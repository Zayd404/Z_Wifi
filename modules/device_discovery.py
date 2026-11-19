import subprocess
import re
import socket
import ipaddress
from colorama import Fore, Style, init
from utils.animation import Loading
from config.settings import BATAS_WAKTU

init(autoreset=True)


def dapatkan_ip_lokal():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        alamat = s.getsockname()[0]
        s.close()
        return alamat
    except Exception:
        return None


def baca_tabel_arp():
    arp_map = {}
    try:
        out = subprocess.check_output(
            ["ip", "neigh"], text=True, stderr=subprocess.DEVNULL
        )
        for line in out.splitlines():
            parts = line.split()
            if len(parts) >= 5 and "lladdr" in parts:
                ip = parts[0]
                mac = parts[parts.index("lladdr") + 1].upper()
                arp_map[ip] = mac
    except Exception:
        pass
    return arp_map


def cari_nama_lengkap(ip, nama_nmap):
    if nama_nmap and nama_nmap != "Tidak diketahui" and nama_nmap != ip:
        return nama_nmap

    try:
        fqdn = socket.getfqdn(ip)
        if fqdn and fqdn != ip:
            return fqdn
    except Exception:
        pass

    return "Tidak diketahui (Privasi Aktif)"


def deteksi_perangkat():
    print()
    print(Fore.GREEN + "=" * 60)
    print("          DETEKSI PERANGKAT JARINGAN")
    print("=" * 60)

    ip_saya = dapatkan_ip_lokal()
    saran_subnet = ""
    if ip_saya:
        prefix = ".".join(ip_saya.split(".")[:3])
        saran_subnet = f"{prefix}.0/24"
        print(Fore.CYAN + f"[i] IP Perangkat Anda : {ip_saya}")
        print(Fore.CYAN + f"[i] Saran Jaringan    : {saran_subnet}")

    prompt = f"\nMasukkan jaringan lokal [{saran_subnet or '192.168.1.0/24'}]: "
    jaringan = input(prompt).strip()

    if not jaringan and saran_subnet:
        jaringan = saran_subnet

    try:
        network = ipaddress.ip_network(jaringan, strict=False)

        if not network.is_private or network.version != 4:
            print(Fore.RED + "\n[!] Gunakan jaringan IPv4 lokal.")
            return

        if network.prefixlen < 24:
            print(Fore.RED + "\n[!] Jangkauan dibatasi maksimal 256 alamat.")
            return

    except ValueError:
        print(Fore.RED + "\n[!] Format jaringan tidak valid.")
        return

    try:
        animasi = Loading("Menganalisis kekuatan sinyal WiFi")
        animasi.mulai()

        try:
            hasil = subprocess.run(
                ["termux-wifi-scaninfo"],
                capture_output=True,
                text=True,
                timeout=20
            )
        finally:
            animasi.berhenti()

        if hasil.returncode != 0:
            print(Fore.RED + "\n[!] Pemeriksaan gagal.")
            print(hasil.stderr)
            return

        arp_lokal = baca_tabel_arp()
        daftar = []
        perangkat = None

        for baris in hasil.stdout.splitlines():
            if baris.startswith("Nmap scan report for "):
                if perangkat:
                    daftar.append(perangkat)

                raw = baris.replace("Nmap scan report for ", "").strip()
                cocok = re.search(r"\(([\d.]+)\)", raw)

                if cocok:
                    alamat_ip = cocok.group(1)
                    nama_nmap = raw.replace(f" ({alamat_ip})", "").strip()
                else:
                    alamat_ip = raw
                    nama_nmap = "Tidak diketahui"

                nama_final = cari_nama_lengkap(alamat_ip, nama_nmap)

                keterangan = ""
                if alamat_ip == ip_saya:
                    keterangan = Fore.YELLOW + " [Perangkat Ini]"
                elif alamat_ip.endswith(".1"):
                    keterangan = Fore.MAGENTA + " [Router/Gateway]"

                mac_awal = arp_lokal.get(alamat_ip, "Dibatasi Android (Non-Root)")

                perangkat = {
                    "ip": alamat_ip,
                    "nama": nama_final,
                    "keterangan": keterangan,
                    "mac": mac_awal,
                    "produsen": "Perlu akses root/admin"
                }

            elif perangkat and "MAC Address:" in baris:
                bagian = baris.split("MAC Address:", 1)[1].strip()
                data_mac = bagian.split(" ", 1)
                perangkat["mac"] = data_mac[0]
                if len(data_mac) > 1:
                    perangkat["produsen"] = data_mac[1].strip("()")

        if perangkat:
            daftar.append(perangkat)

        print(Fore.GREEN + "=" * 60)
        print(f" JUMLAH PERANGKAT TERDETEKSI: {len(daftar)}")
        print("=" * 60)

        for nomor, device in enumerate(daftar, 1):
            print(Fore.CYAN + f"\n[{nomor}] PERANGKAT{device['keterangan']}")
            print(Fore.WHITE + f"    Nama       : {device['nama']}")
            print(f"    Alamat IP  : {device['ip']}")
            print(f"    Alamat MAC : {device['mac']}")
            print(f"    Produsen   : {device['produsen']}")

        print(Fore.GREEN + "\n" + "=" * 60)
        print(Fore.YELLOW + "[INFO] Semua perangkat aktif berhasil dipindai.")

    except subprocess.TimeoutExpired:
        print(Fore.RED + "\n[!] Pemeriksaan melewati batas waktu.")
    except FileNotFoundError:
        print(Fore.RED + "\n[!] Nmap tidak ditemukan.")
    except Exception as error:
        print(Fore.RED + f"\n[!] Kesalahan: {error}")


if __name__ == "__main__":
    deteksi_perangkat()
