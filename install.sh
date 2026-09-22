#!/bin/bash
# INSTALL SCRIPT - © ZenDlouis
# JALANKAN: bash install.sh

echo "╔══════════════════════════════════════╗"
echo "║  🔥 TELEGRAM BUG ATTACKER V13 🔥    ║"
echo "║  © ZenDlouis - Auto Installer       ║"
echo "╚══════════════════════════════════════╝"

echo "[+] Update Termux..."
pkg update -y && pkg upgrade -y

echo "[+] Install Python..."
pkg install python -y

echo "[+] Install dependencies..."
pip install -r requirements.txt

echo "[+] Setup project folder..."
mkdir -p bugs assets

echo "[✅] INSTALL SELESAI!"
echo "[+] Jalankan dengan: python main.py"
