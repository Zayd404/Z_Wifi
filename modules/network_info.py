import json
import subprocess
from utils.animation import Loading
from colorama import Fore, Style


def informasi_jaringan():

    print()
    print(Fore.GREEN + "=" * 60)
    print("             INFORMASI JARINGAN WIFI")
    print("=" * 60)

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
            print(Fore.RED + "[!] Gagal mengambil informasi jaringan.")
            print(hasil.stderr)
            return

        data = json.loads(hasil.stdout)

        if not isinstance(data, dict) or not data:
            print(Fore.YELLOW + "[!] Tidak ada informasi koneksi.")
            return

        frekuensi = data.get("frequency", 0)

        if 2400 <= frekuensi < 2500:
            band = "2.4 GHz"
        elif 5000 <= frekuensi < 5950:
            band = "5 GHz"
        elif 5950 <= frekuensi <= 7125:
            band = "6 GHz"
        else:
            band = "Tidak diketahui"

        informasi = [
            ("SSID", data.get("ssid", "Tidak tersedia")),
            ("BSSID", data.get("bssid", "Tidak tersedia")),
            ("IP Address", data.get("ip", "Tidak tersedia")),
            ("Frekuensi", f"{frekuensi} MHz" if frekuensi else "Tidak tersedia"),
            ("Band", band),
            ("Link Speed", f"{data.get('link_speed', '-')} Mbps"),
            ("Network ID", data.get("network_id", "-")),
            ("Status", data.get("supplicant_state", "Tidak diketahui"))
        ]

        print(Fore.CYAN + "-" * 60)

        for label, nilai in informasi:
            print(f"{label:<18}: {nilai}")

        print(Fore.GREEN + "-" * 60)
        print("[+] Informasi koneksi berhasil dibaca.")

    except FileNotFoundError:
        print(Fore.RED + "[!] Termux:API tidak ditemukan.")

    except subprocess.TimeoutExpired:
        print(Fore.RED + "[!] Waktu pengambilan data habis.")

    except json.JSONDecodeError:
        print(Fore.RED + "[!] Data JSON tidak valid.")

    except Exception as error:
        print(Fore.RED + f"[!] Kesalahan: {error}")


if __name__ == "__main__":
    informasi_jaringan()
