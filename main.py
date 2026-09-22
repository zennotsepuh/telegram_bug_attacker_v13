# -*- coding: utf-8 -*-
# MAIN EXECUTION - © ZenDlouis
# JALANKAN INI BUAT MULAI NGACURIN!

import sys
import time
from colorama import init, Fore

from config import AUTO_RESTART
from banner import Banner
from menu import Menu
from bugs import BugsNetwork, BugsAccount, BugsGroup, BugsUtils

init(autoreset=True)

class TelegramBugAttacker:
    def __init__(self):
        self.banner = Banner()
        self.menu = Menu()
        self.network = BugsNetwork()
        self.account = BugsAccount()
        self.group = BugsGroup()
        self.utils = BugsUtils()
        
        self.bug_map = {
            '1': self.network.spam_flood,
            '2': self.group.group_crasher,
            '3': self.account.account_cloner,
            '4': self.utils.message_deleter,
            '5': self.utils.phishing_generator,
            '6': self.group.channel_hijacker,
            '7': self.utils.voice_spammer,
            '8': self.group.sticker_bomber,
            '9': self.account.user_info_grabber,
            '10': self.group.group_admin_stealer,
            '11': self.utils.message_editor,
            '12': self.network.bot_spammer,
            '13': self.network.url_scanner,
            '14': self.network.call_bomber,
            '15': self.network.ip_logger,
            '16': self.network.mass_dm,
            '17': self.group.group_joiner,
            '18': self.utils.contact_extractor,
            '19': self.utils.media_downloader,
            '20': self.utils.status_viewer,
            '21': self.account.location_spoofer,
            '22': self.account.fake_verification,
            '23': self.account.report_bomber,
            '24': self.utils.chat_cleaner,
            '25': self.account.account_freezer,
            '99': self.utils.auto_destroy
        }

    def run(self):
        while True:
            try:
                self.banner.show()
                self.menu.show()
                
                choice = self.menu.get_prompt()
                
                if choice == '0':
                    print(f"\n{Fore.RED}[💀] KELUAR DARI SYSTEM...")
                    print(f"{Fore.RED}[✅] SAMPAI JUMPA BOSS!")
                    break
                
                if choice in self.bug_map:
                    print(f"\n{Fore.GREEN}[⚡] EXECUTING: {self.menu.get_menu()[choice]['name']}...")
                    time.sleep(0.5)
                    self.bug_map[choice]()
                else:
                    print(f"{Fore.RED}[❌] NOMOR BUG GAK ADA, TOLOL!")
                
                input(f"\n{Fore.CYAN}[>] Tekan Enter buat lanjut...")
                
            except KeyboardInterrupt:
                print(f"\n{Fore.RED}[💀] SISTEM DIHENTIKAN OLEH BOS!")
                break
            except Exception as e:
                print(f"{Fore.RED}[❌] ERROR: {e}")
                if AUTO_RESTART:
                    time.sleep(2)
                    continue
                break

if __name__ == "__main__":
    attacker = TelegramBugAttacker()
    attacker.run()
