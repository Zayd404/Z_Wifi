import json
import subprocess

from colorama import Fore, Style
from modules.wifi_scan import kategori_sinyal
from utils.animation import Loading

def analisis_sinyal():

    print()
    print(Fore.GREEN + "=" * 65)
    print("             ANALISIS KEKUATAN SINYAL")
    print("=" * 65)

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
            print(Fore.RED + "[!] Pemindaian gagal.")
            return

        data = json.loads(hasil.stdout)

        if not isinstance(data, list) or not data:
            print(Fore.YELLOW + "[!] Tidak ada jaringan ditemukan.")
            return

        # Urutkan dari sinyal terkuat ke terlemah
        data.sort(
            key=lambda wifi: wifi.get("rssi", -100),
            reverse=True
        )

        print(Fore.CYAN + "-" * 65)
        print(f"{'NO':<5}{'SSID':<25}{'RSSI':<12}{'KUALITAS'}")
        print("-" * 65)

        for nomor, wifi in enumerate(data, 1):

            ssid = wifi.get("ssid") or "[Tersembunyi]"
            rssi = wifi.get("rssi", -100)
            kualitas = kategori_sinyal(rssi)

            print(
                f"{nomor:<5}"
                f"{ssid[:23]:<25}"
                f"{rssi:<12}"
                f"{kualitas}"
            )

        terkuat = data[0]
        terlemah = data[-1]

        print(Fore.GREEN + "\n" + "-" * 65)

        print(
            f"[+] Sinyal terkuat : "
            f"{terkuat.get('ssid') or '[Tersembunyi]'} "
            f"({terkuat.get('rssi')} dBm)"
        )

        print(
            f"[-] Sinyal terlemah: "
            f"{terlemah.get('ssid') or '[Tersembunyi]'} "
            f"({terlemah.get('rssi')} dBm)"
        )

        print(f"\n[+] Total jaringan dianalisis: {len(data)}")

    except FileNotFoundError:
        print(Fore.RED + "[!] Termux:API tidak ditemukan.")

    except subprocess.TimeoutExpired:
        print(Fore.RED + "[!] Pemindaian melewati batas waktu.")

    except json.JSONDecodeError:
        print(Fore.RED + "[!] Data JSON tidak valid.")

    except Exception as error:
        print(Fore.RED + f"[!] Kesalahan: {error}")


if __name__ == "__main__":
    analisis_sinyal()
