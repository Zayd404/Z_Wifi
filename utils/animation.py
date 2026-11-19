import sys
import time
import threading
from itertools import cycle

from colorama import Fore, Style


class Loading:

    def __init__(self, pesan="Sedang memproses"):
        self.pesan = pesan
        self.berjalan = False
        self.thread = None

    def _animasi(self):

        warna = cycle([
            Fore.GREEN,
            Fore.CYAN,
            Fore.BLUE,
            Fore.MAGENTA,
            Fore.YELLOW
        ])

        titik = cycle(["●", "● ●", "● ● ●", "● ● ● ●"])

        while self.berjalan:
            warna_sekarang = next(warna)
            titik_sekarang = next(titik)

            sys.stdout.write(
                f"\r{warna_sekarang}{self.pesan} {titik_sekarang}   "
            )

            sys.stdout.flush()
            time.sleep(0.25)

        sys.stdout.write("\r" + " " * 65 + "\r")
        sys.stdout.flush()

    def mulai(self):
        self.berjalan = True
        self.thread = threading.Thread(
            target=self._animasi,
            daemon=True
        )
        self.thread.start()

    def berhenti(self):
        self.berjalan = False

        if self.thread:
            self.thread.join()

        print(Style.RESET_ALL, end="")
