import json
import subprocess
from collections import Counter
from utils.animation import Loading
from colorama import Fore, Style


def tentukan_band(freq):
    if 2400 <= freq <= 2500:
        return "2.4 GHz"
    elif 5000 <= freq < 5950:
        return "5 GHz"
    elif 5950 <= freq <= 7125:
        return "6 GHz"
    return "Tidak diketahui"


def hitung_channel(freq):
    if 2412 <= freq <= 2472:
        return (freq - 2407) // 5

    if freq == 2484:
        return 14

    if 5000 <= freq < 5950:
        return (freq - 5000) // 5

    if 5955 <= freq <= 7115:
        return (freq - 5950) // 5

    return "?"


def analisis_channel():

    print()
    print(Fore.GREEN + "=" * 65)
    print("                 ANALISIS CHANNEL WIFI")
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

        jumlah_band = Counter()
        jumlah_channel = Counter()

        print(Fore.CYAN + "-" * 65)
        print(f"{'NO':<5}{'SSID':<25}{'BAND':<12}{'CHANNEL'}")
        print("-" * 65)

        for nomor, wifi in enumerate(data, 1):

            ssid = wifi.get("ssid") or "[Tersembunyi]"
            freq = wifi.get("frequency_mhz", 0)

            band = tentukan_band(freq)
            channel = hitung_channel(freq)

            jumlah_band[band] += 1

            if channel != "?":
                jumlah_channel[(band, channel)] += 1

            print(
                f"{nomor:<5}"
                f"{ssid[:23]:<25}"
                f"{band:<12}"
                f"{channel}"
            )

        print(Fore.GREEN + "\n" + "-" * 65)
        print("RINGKASAN FREKUENSI")

        for band, jumlah in jumlah_band.items():
            print(f"[+] {band:<18}: {jumlah} jaringan")

        print("\nCHANNEL PALING RAMAI")

        if jumlah_channel:
            for (band, channel), jumlah in jumlah_channel.most_common(5):
                print(
                    f"[+] {band} | Channel {channel}: "
                    f"{jumlah} jaringan"
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
    analisis_channel()
