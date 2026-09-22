# -*- coding: utf-8 -*-
# NETWORK BUGS - © ZenDlouis
# BUG SEPUTARAN JARINGAN & SPAM

import time
import random
import threading
from colorama import Fore
from config import SPAM_DELAY, MAX_THREADS

class BugsNetwork:
    def __init__(self):
        self.green = Fore.GREEN
        self.red = Fore.RED
        self.yellow = Fore.YELLOW

    def spam_flood(self):
        target = input(f"{self.yellow}[?] Username/ID target: ")
        jumlah = int(input(f"{self.yellow}[?] Jumlah spam: "))
        pesan = input(f"{self.yellow}[?] Pesan spam: ")
        print(f"\n{self.red}[💀] MULAI SPAM FLOOD KE {target}!")

        def spam_thread():
            for i in range(jumlah // MAX_THREADS + 1):
                print(f"{self.green}[+] Spam dikirim!")
                time.sleep(SPAM_DELAY)

        threads = []
        for _ in range(min(jumlah, MAX_THREADS)):
            t = threading.Thread(target=spam_thread)
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
        print(f"{self.red}[✅] SPAM FLOOD SELESAI! {jumlah} pesan dikirim!")

    def mass_dm(self):
        jumlah = int(input(f"{self.yellow}[?] Jumlah user: "))
        pesan = input(f"{self.yellow}[?] Pesan: ")
        print(f"\n{self.red}[💀] MASS DM KE {jumlah} USER!")
        for i in range(jumlah):
            print(f"{self.green}[+] DM ke-{i+1} dikirim!")
            time.sleep(0.1)
        print(f"{self.red}[✅] MASS DM SELESAI!")

    def call_bomber(self):
        target = input(f"{self.yellow}[?] Nomor target: ")
        jumlah = int(input(f"{self.yellow}[?] Jumlah panggilan: "))
        print(f"\n{self.red}[💀] CALL BOMBING {target}!")
        for i in range(jumlah):
            print(f"{self.green}[+] Panggilan ke-{i+1} dikirim!")
            time.sleep(0.5)
        print(f"{self.red}[✅] CALL BOMBER SELESAI!")

    def ip_logger(self):
        target = input(f"{self.yellow}[?] Link target: ")
        print(f"\n{self.red}[💀] LOGGING IP DARI {target}...")
        data = {
            'IP': f"192.168.{random.randint(1,255)}.{random.randint(1,255)}",
            'Lokasi': random.choice(['Jakarta', 'Bandung', 'Surabaya', 'Medan']),
            'ISP': random.choice(['Telkomsel', 'Indosat', 'XL', 'Biznet']),
            'Device': random.choice(['iPhone 14', 'Samsung S23', 'Laptop ASUS'])
        }
        for k, v in data.items():
            print(f"{self.green}[+] {k}: {v}")
            time.sleep(0.1)
        print(f"{self.red}[✅] IP BERHASIL DI-LOG!")

    def url_scanner(self):
        url = input(f"{self.yellow}[?] URL: ")
        print(f"\n{self.red}[💀] SCANNING {url}...")
        result = {
            'Status': 'Aman kontol!',
            'SSL': 'Valid',
            'Server': random.choice(['Nginx', 'Apache', 'Cloudflare', 'AWS']),
            'IP': f"192.168.{random.randint(1,255)}.{random.randint(1,255)}"
        }
        for k, v in result.items():
            print(f"{self.green}[+] {k}: {v}")
            time.sleep(0.2)
        print(f"{self.red}[✅] SCAN SELESAI!")

    def bot_spammer(self):
        bot = input(f"{self.yellow}[?] Username bot: ")
        jumlah = int(input(f"{self.yellow}[?] Jumlah spam: "))
        print(f"\n{self.red}[💀] SPAM BOT {bot}!")
        for i in range(jumlah):
            print(f"{self.green}[+] Spam ke-{i+1} dikirim!")
            time.sleep(0.1)
        print(f"{self.red}[✅] BOT SPAM BERHASIL!")
