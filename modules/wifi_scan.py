import json
import subprocess
from colorama import Fore, Style
from utils.animation import Loading
from modules.history import simpan_riwayat

def kategori_sinyal(rssi):
    if rssi >= -50:
        return "Sangat Kuat"
    elif rssi >= -60:
        return "Kuat"
    elif rssi >= -70:
        return "Sedang"
    elif rssi >= -80:
        return "Lemah"
    else:
        return "Sangat Lemah"


def hitung_channel(frekuensi):
    if 2412 <= frekuensi <= 2484:
        return (frekuensi - 2407) // 5

    elif 5000 <= frekuensi <= 5895:
        return (frekuensi - 5000) // 5

    elif 5955 <= frekuensi <= 7115:
        return (frekuensi - 5950) // 5

    return "Tidak diketahui"


def scan_wifi():

    print()
    print(Fore.GREEN + "=" * 75)
    print("                  PEMINDAIAN WIFI SEKITAR")
    print("=" * 75)

    animasi = Loading("Memindai jaringan WiFi")
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

    try:

        if hasil.returncode != 0:
            print(Fore.RED + "[!] Gagal menjalankan pemindaian.")
            print(hasil.stderr)
            return

        data = json.loads(hasil.stdout)

        if not isinstance(data, list):
            print(Fore.RED + "[!] Format data tidak valid.")
            return

        if not data:
            print(Fore.YELLOW + "[!] Tidak ada jaringan ditemukan.")
            return

        simpan_riwayat(data)

        print(Fore.CYAN + "-" * 75)

        print(
            f"{'NO':<4}"
            f"{'SSID':<20}"
            f"{'RSSI':<9}"
            f"{'CHANNEL':<10}"
            f"{'FREKUENSI':<13}"
            f"{'SINYAL'}"
        )

        print("-" * 75)

        for nomor, wifi in enumerate(data, 1):

            ssid = wifi.get("ssid") or "[SSID Tersembunyi]"
            rssi = wifi.get("rssi", 0)
            frekuensi = wifi.get("frequency_mhz", 0)

            channel = hitung_channel(frekuensi)
            sinyal = kategori_sinyal(rssi)

            print(
                f"{nomor:<4}"
                f"{ssid[:18]:<20}"
                f"{rssi:<9}"
                f"{channel!s:<10}"
                f"{frekuensi:<13}"
                f"{sinyal}"
            )

        print(Fore.GREEN + "-" * 75)
        print(f"[+] Total jaringan ditemukan: {len(data)}")

    except FileNotFoundError:
        print(Fore.RED + "[!] Termux:API tidak ditemukan.")

    except subprocess.TimeoutExpired:
        print(Fore.RED + "[!] Pemindaian melewati batas waktu.")

    except json.JSONDecodeError:
        print(Fore.RED + "[!] Data JSON tidak dapat dibaca.")

    except Exception as error:
        print(Fore.RED + f"[!] Terjadi kesalahan: {error}")


if __name__ == "__main__":
    scan_wifi()
