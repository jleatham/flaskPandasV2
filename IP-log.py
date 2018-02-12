import time
import os
import re
import datetime
import requests

port = '5000'
directory = '/home/cisco/houston-pos-v2/'
#directory = '/Users/jleatham/Documents/Programming/Python/automation/POS/on linux server v2/flaskPandasV2/'
version = '2' # main vs main2 etc, for main.py use ''




def log_ip():
    ip_list=[]
    #f = open(directory+"pos_log.out","r")
    f = open(directory+"temp.txt","r")
    lines = f.readlines()
    f.close()
    #print("starting loop")
    for line in lines:
        #print(line)
        m = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",line)
        #m = re.findall("10.99.189.117",line)
        #print(m)
        #print(m)
        if len(m) > 0:
            print(m)
            ip_list.append(m[0])
    #print("finished loop")  
    ip_list = list(set(ip_list))  
    print("IP List:\n\n" +str(ip_list))
    print("\n\nIP count: "+str(len(ip_list)))


log_ip()
print("hello")