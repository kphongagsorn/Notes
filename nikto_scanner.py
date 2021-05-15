# Scans list of URLs with Nikto 

from urllib.parse import urlparse
from typing import Set, List
from datetime import date
from subprocess import PIPE
from multiprocessing import Pool
import multiprocessing
import psutil
import os
import re
import datetime
import time
import argparse
import requests
import json
import subprocess
import logging

logging.basicConfig(level=logging.DEBUG)

class Nikto:
    def nikto(self, target_uri):
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:86.0)'
        p = subprocess.call('perl /pathtomodifiedniktoorcallniktodirectly/nikto.pl -useproxy http://127.0.0.1:8081/ -useragent "%s" -C all -h %s -o . -Format xml '%(user_agent, target_uri), shell=True, stdout=PIPE, stderr=PIPE) 
        return p

if __name__ == "__main__":
    nikto = Nikto()
    pool_num=multiprocessing.cpu_count()-1
    #pool_num=2
    pool = Pool(pool_num)
    target_list=['www.google.com','www.amazon.com','facebook.com']

    try:
        print('[+] Simultaneous Nikto Processes: %i' %(pool_num))
        print('[+] Target list size: %i' %(len(target_list)))
        print('[+] Scanning target list...')
        pool.map(nikto.nikto,target_list)
    finally:
        pool.close()
        pool.join()

    print('[+] Done!')