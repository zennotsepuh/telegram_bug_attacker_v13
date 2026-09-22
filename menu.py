# -*- coding: utf-8 -*-
# MENU DISPLAY - © ZenDlouis
# DAFTAR BUG & TAMPILAN MENU

from colorama import Fore, Style

class Menu:
    def __init__(self):
        self.red = Fore.RED
        self.green = Fore.GREEN
        self.yellow = Fore.YELLOW
        self.cyan = Fore.CYAN
        self.white = Fore.WHITE
        self.magenta = Fore.MAGENTA
        self.reset = Style.RESET_ALL

        self.bug_menu = {
            '1':  {'name': '🔻 SPAM FLOOD',          'desc': 'Ban spam 1000 pesan/detik'},
            '2':  {'name': '🔻 GROUP CRASHER',       'desc': 'Bikin group crash total'},
            '3':  {'name': '🔻 ACCOUNT CLONER',      'desc': 'Clone akun target'},
            '4':  {'name': '🔻 MESSAGE DELETER',     'desc': 'Hapus semua chat target'},
            '5':  {'name': '🔻 PHISHING GENERATOR',  'desc': 'Bikin link phishing mewah'},
            '6':  {'name': '🔻 CHANNEL HIJACKER',    'desc': 'Rekrut channel orang'},
            '7':  {'name': '🔻 VOICE SPAMMER',       'desc': 'Spam voice note'},
            '8':  {'name': '🔻 STICKER BOMBER',      'desc': 'Bom stiker 500+'},
            '9':  {'name': '🔻 USER INFO GRABBER',   'desc': 'Ambil semua data user'},
            '10': {'name': '🔻 GROUP ADMIN STEALER', 'desc': 'Curi hak admin'},
            '11': {'name': '🔻 MESSAGE EDITOR',      'desc': 'Edit pesan orang'},
            '12': {'name': '🔻 BOT SPAMMER',         'desc': 'Spam bot sampe mati'},
            '13': {'name': '🔻 URL SCANNER',         'desc': 'Scan link berbahaya'},
            '14': {'name': '🔻 CALL BOMBER',         'desc': 'Bom panggilan 24/7'},
            '15': {'name': '🔻 IP LOGGER',           'desc': 'Capture IP target'},
            '16': {'name': '🔻 MASS DM',             'desc': 'DM 1000 orang sekaligus'},
            '17': {'name': '🔻 GROUP JOINER',        'desc': 'Join 1000 group otomatis'},
            '18': {'name': '🔻 CONTACT EXTRACTOR',   'desc': 'Ambil semua kontak target'},
            '19': {'name': '🔻 MEDIA DOWNLOADER',    'desc': 'Download semua media'},
            '20': {'name': '🔻 STATUS VIEWER',       'desc': 'View status tanpa ketahuan'},
            '21': {'name': '🔻 LOCATION SPOOFER',    'desc': 'Palsuin lokasi target'},
            '22': {'name': '🔻 FAKE VERIFICATION',   'desc': 'Bikin centang palsu'},
            '23': {'name': '🔻 REPORT BOMBER',       'desc': 'Report akun sampe banned'},
            '24': {'name': '🔻 CHAT CLEANER',        'desc': 'Hapus semua chat target'},
            '25': {'name': '🔻 ACCOUNT FREEZER',     'desc': 'Freeze akun target'},
            '99': {'name': '⚡ AUTO DESTROY',         'desc': 'Hancurkan semua!'}
        }

    def show(self):
        print(f"{self.cyan}╔═══════════════════════════════════════════════════════╗")
        print(f"{self.cyan}║  {self.red}💀 BUG MENU - 200+ OPTIONS SIAP DIPAKAI 💀{self.cyan}    ║")
        print(f"{self.cyan}╚═══════════════════════════════════════════════════════╝")
        print()
        for key, value in self.bug_menu.items():
            print(f"{self.yellow}[{key:>2}] {self.white}{value['name']:<25} {self.cyan}- {value['desc']}")
        print()
        print(f"{self.magenta}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{self.red}[ 0] KELUAR - KALO BERANI KELUAR!")
        print(f"{self.magenta}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    def get_menu(self):
        return self.bug_menu

    def get_prompt(self):
        return input(f"\n{self.yellow}[>] Pilih bug (nomor): {self.white}")
