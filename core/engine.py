
from core.banner import banner
from core.menu import tampilkan_menu
from config.settings import NAMA_TOOL, VERSI
from utils.colors import HIJAU, KUNING, MERAH, RESET
from utils.helpers import bersihkan_layar, garis, jeda
from modules.wifi_scan import scan_wifi
from modules.signal import analisis_sinyal
from modules.channel import analisis_channel
from modules.network_info import informasi_jaringan
from modules.history import tampilkan_riwayat
from modules.device_discovery import deteksi_perangkat


def jalankan_sistem():

    bersihkan_layar()
    banner()

    while True:

        try:
            pilihan = tampilkan_menu()

            if pilihan == "1":
                scan_wifi()
                jeda()

            elif pilihan == "2":
                analisis_sinyal()
                jeda()

            elif pilihan == "3":
                analisis_channel()
                jeda()

            elif pilihan == "4":
                informasi_jaringan()
                jeda()

            elif pilihan == "5":
                tampilkan_riwayat()
                jeda()

            elif pilihan == "6":
                deteksi_perangkat()
                jeda()

            elif pilihan == "0":
                print("\n[!] WIFI_SCANNER dihentikan.")
                break

            else:
                print("\n[!] Pilihan tidak tersedia.")

        except KeyboardInterrupt:
            print("\n\n[!] Proses dibatalkan pengguna.")

        except Exception as error:
            print(f"\n[!] Terjadi kesalahan: {error}")


if __name__ == "__main__":
    jalankan_sistem()
