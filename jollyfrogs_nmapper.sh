#!/bin/bash

#based of jolly frog's nmap strings
#https://community.infosecinstitute.com/discussion/110760/oscp-jollyfrogs-tale-3

echo "target: $1"

echo "running discovery scan..."
#quick discovery scan
nmap -Pn -F -sSU -T5 -oX $1-discovery.xml $1 | grep -v 'filtered|closed' >  $1-discovery.txt

echo "running udp full scan..."
echo "can take up to 4 minutes per host"
#Then force-scan all ports UDP + TCP per host (takes about 4 minutes per host on a LAN or roughly 17 hours for 254 hosts):
nmap -Pn -sSU -T4 -p1-65535 -oX $1-udp-full.xml "$1" | grep -v 'filtered|closed' > $1-udp-full.txt

echo "running tcp full scan from discovered open ports..."
#Then run an intensive scan on the open ports per host, TCP and UDP separately to speed scan up:
nmap -nvv -Pn -sSV -T1 -p$(cat $1-discovery.xml | grep portid | grep protocol=\"tcp\" | cut -d'"' -f4 | paste -sd "," -) --version-intensity 9 -oX $1-full.xml $1

#nmap -nvv -Pn -sUV -T1 -p$(cat 10.1.1.110.xml | grep portid | grep protocol=\"udp\" | cut -d'"' -f4 | paste -sd "," -) --version-intensity 9 -oX /root/10.1.1.110-intense-udp.xml 10.1.1.110
echo "done!"
