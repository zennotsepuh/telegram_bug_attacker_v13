# -*- coding: utf-8 -*-
# GROUP BUGS - © ZenDlouis
# BUG SEPUTARAN GROUP & CHANNEL

import time
import random
from colorama import Fore

class BugsGroup:
    def __init__(self):
        self.green = Fore.GREEN
        self.red = Fore.RED
        self.yellow = Fore.YELLOW

    def group_crasher(self):
        group_id = input(f"{self.yellow}[?] ID grup target: ")
        jumlah = int(input(f"{self.yellow}[?] Jumlah bot crash: "))
        print(f"\n{self.red}[💀] CRASHING GROUP {group_id} DENGAN {jumlah} BOT!")
        for i in range(jumlah):
            print(f"{self.green}[+] Bot {i+1} masuk dan spam!")
            time.sleep(0.3)
        print(f"{self.red}[✅] GROUP BERHASIL DI-CRASH!")

    def channel_hijacker(self):
        channel = input(f"{self.yellow}[?] Username channel: ")
        print(f"\n{self.red}[💀] HIJACKING CHANNEL {channel}...")
        steps = ['Mencuri hak admin...', 'Mengambil alih kontrol...', 'Mengganti owner...', 'Lock channel...']
        for s in steps:
            print(f"{self.green}[+] {s}")
            time.sleep(0.5)
        print(f"{self.red}[✅] CHANNEL BERHASIL DI-HIJACK!")

    def group_admin_stealer(self):
        group = input(f"{self.yellow}[?] ID group: ")
        print(f"\n{self.red}[💀] STEALING ADMIN RIGHTS DI {group}...")
        steps = ['Menyusup sebagai admin...', 'Mengambil alih kontrol...', 'Hapus admin lain...', 'Lock group...']
        for s in steps:
            print(f"{self.green}[+] {s}")
            time.sleep(0.5)
        print(f"{self.red}[✅] ADMIN BERHASIL DI-STEAL!")

    def group_joiner(self):
        jumlah = int(input(f"{self.yellow}[?] Jumlah group: "))
        print(f"\n{self.red}[💀] JOIN {jumlah} GROUP!")
        for i in range(jumlah):
            print(f"{self.green}[+] Join group ke-{i+1}!")
            time.sleep(0.2)
        print(f"{self.red}[✅] GROUP JOINER SELESAI!")

    def sticker_bomber(self):
        group = input(f"{self.yellow}[?] ID group: ")
        jumlah = int(input(f"{self.yellow}[?] Jumlah sticker: "))
        stickers = ['🤡', '💀', '🔥', '😈', '👾', '🎯', '💣', '🔫', '🗡️', '🪓', '💩', '🤮']
        print(f"\n{self.red}[💀] BOM STICKER DI {group}!")
        for i in range(jumlah):
            s = random.choice(stickers)
            print(f"{self.green}[+] Sticker {s} ke-{i+1} dikirim!")
            time.sleep(0.05)
        print(f"{self.red}[✅] STICKER BOMBER SELESAI!")
