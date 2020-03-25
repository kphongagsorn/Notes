#!/bin/bash

# get ips from list of hostnames
# need to clean up error message

while read ip;
do
    #printf "%-4s", $ip
    nslookup $ip | grep -i non-authoritative -A 2 | grep -i address | cut -f 2 -d ":"
done < hostnames.txt
print "done!"
