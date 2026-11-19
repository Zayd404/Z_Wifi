
from config.settings import NAMA_TOOL, VERSI, PEMBUAT
from colorama import Fore, Style


def banner():

    print(Fore.CYAN + r"""
 _       ________________   _____ _________    _   ___   ____________
| |     / /  _/ ____/  _/  / ___// ____/   |  / | / / | / / ____/ __ \
| | /| / // // /_   / /    \__ \/ /   / /| | /  |/ /  |/ / __/ / /_/ /
| |/ |/ // // __/ _/ /    ___/ / /___/ ___ |/ /|  / /|  / /___/ _, _/
|__/|__/___/_/   /___/   /____/\____/_/  |_/_/ |_/_/ |_/_____/_/ |_|
""")

    print(Fore.GREEN + f"""
       🔎 {NAMA_TOOL} - NETWORK DISCOVERY
              Versi : {VERSI}
           By: {PEMBUAT}

############################################################
""" + Style.RESET_ALL)

