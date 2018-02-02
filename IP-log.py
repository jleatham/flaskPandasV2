import schedule
import time
import os
import re
import datetime
import requests

port = '5000'
directory = '/home/cisco/houston-pos-v2/'
version = '2' # main vs main2 etc, for main.py use ''




def log_ip():
    ip_list=[]
    f = open(directory+"pos_log.out","r")
    lines = f.readlines()
    f.close()
    #print("starting loop")
    for line in lines:
        m = re.findall("\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b",line)
        if m:
            print(m)
    #print("finished loop")    


log_ip()
