# -*- coding: utf-8 -*-
# UTILITY BUGS - © ZenDlouis
# BUG TAMBAHAN & UTILITIES

import time
import random
from colorama import Fore

class BugsUtils:
    def __init__(self):
        self.green = Fore.GREEN
        self.red = Fore.RED
        self.yellow = Fore.YELLOW

    def message_deleter(self):
        chat_id = input(f"{self.yellow}[?] ID chat: ")
        print(f"\n{self.red}[💀] MENGHAPUS SEMUA PESAN DI {chat_id}...")
        for i in range(100):
            print(f"{self.green}[+] Pesan ke-{i+1} dihapus!")
            if i % 10 == 0:
                time.sleep(0.05)
        print(f"{self.red}[✅] SEMUA PESAN DIHAPUS!")

    def message_editor(self):
        chat = input(f"{self.yellow}[?] ID chat: ")
        msg_id = input(f"{self.yellow}[?] ID pesan: ")
        new_msg = input(f"{self.yellow}[?] Pesan baru: ")
        print(f"\n{self.red}[💀] EDITING PESAN DI {chat}...")
        time.sleep(1)
        print(f"{self.green}[+] Pesan {msg_id} diedit!")
        print(f"{self.green}[+] Pesan baru: {new_msg}")
        print(f"{self.red}[✅] EDIT PESAN BERHASIL!")

    def voice_spammer(self):
        target = input(f"{self.yellow}[?] Target: ")
        jumlah = int(input(f"{self.yellow}[?] Jumlah voice: "))
        print(f"\n{self.red}[💀] SPAM VOICE NOTE KE {target}!")
        for i in range(jumlah):
            print(f"{self.green}[+] Voice {i+1} dikirim!")
            time.sleep(0.1)
        print(f"{self.red}[✅] VOICE SPAM SELESAI!")

    def phishing_generator(self):
        url = input(f"{self.yellow}[?] URL palsu: ")
        print(f"\n{self.red}[💀] GENERATING PHISHING LINK...")
        print(f"{self.green}[+] Link: {url}")
        templates = ['Login Facebook', 'Login Instagram', 'Login WhatsApp', 'Login Telegram', 'Login Bank']
        for t in templates:
            print(f"{self.green}[+] Template {t}: Siap!")
            time.sleep(0.2)
        print(f"{self.red}[✅] LINK PHISHING SIAP DIPAKAI!")

    def contact_extractor(self):
        target = input(f"{self.yellow}[?] Target: ")
        print(f"\n{self.red}[💀] EXTRACTING CONTACTS DARI {target}...")
        for i in range(100):
            phone = f"+628{random.randint(100000000,999999999)}"
            name = f"User_{random.randint(1000,9999)}"
            print(f"{self.green}[+] {i+1}. {name} - {phone}")
            time.sleep(0.01)
        print(f"{self.red}[✅] CONTACT EXTRACTOR SELESAI!")

    def media_downloader(self):
        chat = input(f"{self.yellow}[?] ID chat: ")
        print(f"\n{self.red}[💀] DOWNLOADING MEDIA DARI {chat}...")
        media = ['Photo', 'Video', 'Audio', 'Document', 'GIF']
        for i in range(50):
            m = random.choice(media)
            size = f"{random.randint(100,5000)}KB"
            print(f"{self.green}[+] {m} ke-{i+1} - {size} didownload!")
            time.sleep(0.1)
        print(f"{self.red}[✅] MEDIA DOWNLOADER SELESAI!")

    def status_viewer(self):
        target = input(f"{self.yellow}[?] Username target: ")
        print(f"\n{self.red}[💀] VIEWING STATUS {target}...")
        statuses = ['Online', 'Offline', 'Recently', 'Last seen recently']
        bio = ['Gapunya bio', 'Anak ngentot', 'Ganteng', 'Cape', 'Mager']
        print(f"{self.green}[+] Status: {random.choice(statuses)}")
        print(f"{self.green}[+] Bio: {random.choice(bio)}")
        print(f"{self.green}[+] Online: {random.choice(['Iya', 'Tidak'])}")
        print(f"{self.red}[✅] STATUS VIEWER SELESAI!")

    def chat_cleaner(self):
        target = input(f"{self.yellow}[?] Target: ")
        print(f"\n{self.red}[💀] CLEANING CHAT {target}...")
        for i in range(100):
            print(f"{self.green}[+] Chat ke-{i+1} dihapus!")
            time.sleep(0.01)
        print(f"{self.red}[✅] CHAT CLEANER SELESAI!")

    def auto_destroy(self):
        print(f"\n{self.red}[💀] AUTO DESTROY ACTIVATED! HANCURKAN SEMUA!")
        for i in range(101):
            print(f"\r{self.red}[+] Menghancurkan sistem {i}%", end='')
            time.sleep(0.05)
        print(f"\n{self.red}[✅] SEMUA HANCUR! DUNIA MAY HANCUR!")
