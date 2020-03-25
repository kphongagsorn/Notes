#!/bin/bash

for ip in `cat ./hostnames.txt`;
do
    printf "%-4s", $ip
    nslookup $ip | awk -F"=" '/name/{print$2}'
    echo ""
done > ips.txt
