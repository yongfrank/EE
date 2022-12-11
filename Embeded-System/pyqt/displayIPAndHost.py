'''
Author: Frank Chu
Date: 2022-12-11 12:01:45
LastEditors: Frank Chu
LastEditTime: 2022-12-11 12:16:11
FilePath: /EE/Embeded-System/pyqt/displayIPAndHost.py
Description: 

Copyright (c) 2022 by Frank Chu, All Rights Reserved. 
'''
# https://www.geeksforgeeks.org/display-hostname-ip-address-python/

import socket
import cpuinfo
import platform

def get_platform():
    platform_info = platform.platform()
    print("System :", platform_info)

def get_host_name_and_ip():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        print("Hostname :", host_name)
        print("IP :", host_ip)
    except:
        print("Unable to get Hostname and IP")

def get_cpu_info():
    '''
    Getting processor information in Python
    https://stackoverflow.com/questions/4842448/getting-processor-information-in-python
    '''
    
    info = cpuinfo.get_cpu_info()
    print("\n#################### CPU Info ####################")
    for item in info:
        print(item, ":", info[item])
    print("#################### CPU Info ####################\n")
    # print(info)

# driver code
get_platform()
get_host_name_and_ip() # Function call
get_cpu_info()

