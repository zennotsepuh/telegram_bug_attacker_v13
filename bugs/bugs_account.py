# -*- coding: utf-8 -*-
# ACCOUNT BUGS - © ZenDlouis
# BUG SEPUTARAN AKUN TARGET

import time
import random
from colorama import Fore

class BugsAccount:
    def __init__(self):
        self.green = Fore.GREEN
        self.red = Fore.RED
        self.yellow = Fore.YELLOW

    def account_cloner(self):
        target = input(f"{self.yellow}[?] Username target: ")
        print(f"\n{self.red}[💀] CLONING AKUN {target}...")
        steps = ['Profil dicuri!', 'Foto diambil!', 'Bio dicopy!', 'Setting diganti!', 'Password diubah!']
        for step in steps:
            print(f"{self.green}[+] {step}")
            time.sleep(0.5)
        print(f"{self.red}[✅] AKUN BERHASIL DI-CLONE!")

    def user_info_grabber(self):
        target = input(f"{self.yellow}[?] Username target: ")
        print(f"\n{self.red}[💀] GRAB INFO USER {target}...")
        info = {
            'ID': '123456789',
            'Nama': 'Kontol Kece',
            'Bio': 'Anak ngentot',
            'No HP': '+628' + ''.join([str(random.randint(0,9)) for _ in range(10)]),
            'Email': 'kontol@gmail.com',
            'IP': f"192.168.{random.randint(1,255)}.{random.randint(1,255)}",
            'Device': random.choice(['iPhone 14', 'Samsung S23', 'Xiaomi 13', 'Pixel 7']),
            'OS': random.choice(['iOS 16', 'Android 13', 'Android 14'])
        }
        for k, v in info.items():
            print(f"{self.green}[+] {k}: {v}")
            time.sleep(0.1)
        print(f"{self.red}[✅] SEMUA INFO BERHASIL DICURI!")

    def account_freezer(self):
        target = input(f"{self.yellow}[?] Username target: ")
        print(f"\n{self.red}[💀] FREEZING AKUN {target}...")
        steps = ['Mengirim request...', 'Membekukan akun...', 'Menonaktifkan sementara...', 'Lock akun...']
        for s in steps:
            print(f"{self.green}[+] {s}")
            time.sleep(0.5)
        print(f"{self.red}[✅] AKUN BERHASIL DI-FREEZE!")

    def fake_verification(self):
        target = input(f"{self.yellow}[?] Username target: ")
        print(f"\n{self.red}[💀] CREATING FAKE VERIFICATION...")
        print(f"{self.green}[+] Centang biru: ✅")
        print(f"{self.green}[+] Badge: Premium")
        print(f"{self.red}[✅] FAKE VERIFICATION BERHASIL!")

    def report_bomber(self):
        target = input(f"{self.yellow}[?] Username target: ")
        jumlah = int(input(f"{self.yellow}[?] Jumlah report: "))
        print(f"\n{self.red}[💀] REPORT BOMBING {target}!")
        for i in range(jumlah):
            print(f"{self.green}[+] Report ke-{i+1} dikirim!")
            time.sleep(0.1)
        print(f"{self.red}[✅] REPORT BOMBER SELESAI! AKUN BAKAL BANNED!")

    def location_spoofer(self):
        target = input(f"{self.yellow}[?] Target: ")
        print(f"\n{self.red}[💀] SPOOFING LOCATION {target}...")
        print(f"{self.green}[+] Fake GPS: -6.2088, 106.8456")
        print(f"{self.green}[+] Lokasi: Jakarta, Indonesia")
        print(f"{self.red}[✅] LOCATION SPOOFED!")
