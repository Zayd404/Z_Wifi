import json
from pathlib import Path
from utils.animation import Loading
from config.settings import FOLDER_LAPORAN
from datetime import datetime
from colorama import Fore, Style

FOLDER_REPORT = Path(FOLDER_LAPORAN)


def simpan_riwayat(data):

    try:
        FOLDER_REPORT.mkdir(parents=True, exist_ok=True)

        waktu = datetime.now()
        nama_file = waktu.strftime("scan_%Y%m%d_%H%M%S.json")

        laporan = {
            "tanggal": waktu.strftime("%Y-%m-%d"),
            "waktu": waktu.strftime("%H:%M:%S"),
            "total_jaringan": len(data),
            "jaringan": data
        }

        lokasi = FOLDER_REPORT / nama_file

        with open(lokasi, "w", encoding="utf-8") as file:
            json.dump(laporan, file, indent=4, ensure_ascii=False)

        print(Fore.GREEN + f"\n[+] Laporan tersimpan: {lokasi}")

        return True

    except Exception as error:
        print(Fore.RED + f"\n[!] Gagal menyimpan laporan: {error}")
        return False


def tampilkan_riwayat():

    print()
    print(Fore.GREEN + "=" * 65)
    print("                  RIWAYAT PEMINDAIAN")
    print("=" * 65)

    FOLDER_REPORT.mkdir(parents=True, exist_ok=True)

    daftar_file = sorted(
        FOLDER_REPORT.glob("scan_*.json"),
        reverse=True
    )

    if not daftar_file:
        print(Fore.YELLOW + "\n[!] Belum ada riwayat pemindaian.")
        return

    for nomor, lokasi in enumerate(daftar_file, 1):

        try:
            with open(lokasi, "r", encoding="utf-8") as file:
                laporan = json.load(file)

            print(
                f"\n[{nomor}] "
                f"{laporan.get('tanggal', '-')}"
                f" | {laporan.get('waktu', '-')}"
            )

            print(
                f"    Total jaringan: "
                f"{laporan.get('total_jaringan', 0)}"
            )

            print(f"    File: {lokasi.name}")

        except (OSError, json.JSONDecodeError):
            print(Fore.RED + f"\n[!] File bermasalah: {lokasi.name}")

    print(Fore.GREEN + "\n" + "=" * 65)


if __name__ == "__main__":
    tampilkan_riwayat()
