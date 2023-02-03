#!/bin/bash

# prep
apt-get -y update
apt-get -y install python3 git python3-pip curl wget

# sublime
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/sublimehq-archive.gpg > /dev/null
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
apt-get install -y sublime-text

# gdb, radare2
apt-get install -y gdb radare2

# pwndbg
git clone https://github.com/pwndbg/pwndbg
cd pwndbg
./setup.sh

# pwntools
apt-get install python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade pwntools

# ropgadget
python3 -m pip install ROPgadget 
