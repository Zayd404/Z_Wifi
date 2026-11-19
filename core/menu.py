from colorama import Fore, Style
from config.settings import MENU_UTAMA

def tampilkan_menu():

    while True:

        print()
        print(Fore.GREEN + Style.BRIGHT + "=" * 55)
        print("                 MENU UTAMA")
        print("=" * 55)

        print(Fore.CYAN)

        for nomor, nama_menu in enumerate(MENU_UTAMA, 1):
          print(f" [{nomor}] {nama_menu}")

        print("\n [0] Keluar")

        print(Fore.GREEN + "=" * 55)

        pilihan = input(
            Fore.YELLOW + " Pilih Menu > "
        ).strip()

        if pilihan in ["0", "1", "2", "3", "4", "5", "6"]:
            return pilihan

        print(Fore.RED + "\n[!] Pilihan tidak tersedia!")

