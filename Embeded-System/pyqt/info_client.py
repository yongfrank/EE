'''
Author: Frank Chu
Date: 2022-12-11 14:49:38
LastEditors: Frank Chu
LastEditTime: 2022-12-11 16:47:20
FilePath: /EE/Embeded-System/pyqt/info_client.py
Description: 

Copyright (c) 2022 by Frank Chu, All Rights Reserved. 
'''
import socket
import sys
import pickle

class SendInfo:
    def __init__(self, cpu_info, host_name, ip_address, platform_info):
        self.cpu_info = cpu_info
        self.host_name = host_name
        self.ip_address = ip_address
        self.platform_info = platform_info

def connectAndPrint(host_to_connect):
    print("connecting to", host_to_connect)

    with socket.socket() as client_socket:
        client_socket.connect((host_to_connect, 12345))
        
        data = client_socket.recv(4096)
        data_variable = pickle.loads(data)
        
        attributes = vars(data_variable)
        for key, value in attributes.items():
            print(key, ":", value)
    # In Python, the variables inside a with statement will not be destroyed when the with block ends. Instead, the variables will continue to exist in the scope where they were defined, and can be accessed and used after the with block ends.
    return data_variable

if __name__ == "__main__":
    ip_to_connect = sys.argv[1]
    connectAndPrint(ip_to_connect)