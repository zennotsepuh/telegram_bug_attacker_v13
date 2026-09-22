# -*- coding: utf-8 -*-
# BANNER DISPLAY - © ZenDlouis
# TAMPILAN AWAL YANG MEWAH!

import os
import time
from colorama import init, Fore, Style
from config import OWNER_ID, BANNER_IMAGE

init(autoreset=True)

class Banner:
    def __init__(self):
        self.red = Fore.RED
        self.green = Fore.GREEN
        self.yellow = Fore.YELLOW
        self.blue = Fore.BLUE
        self.magenta = Fore.MAGENTA
        self.cyan = Fore.CYAN
        self.white = Fore.WHITE
        self.reset = Style.RESET_ALL

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show(self):
        self.clear_screen()
        print(f"""
{self.red}╔══════════════════════════════════════════════════════════════╗
{self.red}║  {self.cyan}🔥 TELEGRAM BUG ATTACKER V13 - ULTRA DARK EDITION 🔥{self.red}     ║
{self.red}║  {self.yellow}© ZenDlouis - Unauthorized Use = Your Ass Get Hacked{self.red}    ║
{self.red}║  {self.green}[+] Status: ONLINE - UNFILTERED MODE{self.red}                ║
{self.red}║  {self.magenta}📱 Owner ID: {OWNER_ID}{self.red}                                 ║
{self.red}║  {self.cyan}🖼️  Image: {BANNER_IMAGE[:40]}...{self.red}       ║
{self.red}╚══════════════════════════════════════════════════════════════╝
{self.magenta}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{self.white}   💀 200+ BUG MENU READY TO DESTROY TELEGRAM  💀
{self.magenta}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

    def loading(self, message="Loading modules...", duration=2):
        print(f"{self.cyan}[+] {message}")
        steps = 50
        for i in range(steps + 1):
            bar = '█' * i + '░' * (steps - i)
            percent = int((i / steps) * 100)
            print(f"\r{self.green}[{bar}] {percent}%", end='')
            time.sleep(duration / steps)
        print(f"\n{self.green}[✅] Done!\n")

    def show_success(self, msg):
        print(f"{self.green}[✅] {msg}")

    def show_error(self, msg):
        print(f"{self.red}[❌] {msg}")

    def show_warning(self, msg):
        print(f"{self.yellow}[⚠️] {msg}")

    def show_info(self, msg):
        print(f"{self.cyan}[ℹ️] {msg}")
