import socket
import platform
import pickle

host = '0.0.0.0'
port = 12345

class SendInfo:

    def __init__(self, cpu_info, host_name, ip_address, platform_info):
        self.cpu_info = cpu_info
        self.host_name = host_name
        self.ip_address = ip_address
        self.platform_info = platform_info

cpu_info = platform.processor() 
host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)
platform_info = platform.platform()

info_to_be_send = SendInfo(cpu_info, host_name, ip_address, platform_info)
# https://stackoverflow.com/questions/15190362/sending-a-dictionary-using-sockets-in-python
data_string = pickle.dumps(info_to_be_send)
print("Please connect to", ip_address)

with socket.socket() as server_socket:
    server_socket.bind((host, port))
    server_socket.listen()

    while True:
         client_socket, address = server_socket.accept()
         client_socket.send(data_string)

# import socket
# import platform

# host = '0.0.0.0'
# port = 12345

# cpu_info = platform.processor() 
# host_name = socket.gethostname()
# ip_address = socket.gethostbyname(host_name)
# platform_info = platform.platform()

# with socket.socket() as server_socket:
#     server_socket.bind((host, port))
#     server_socket.listen()

#     while True:
#          client_socket, address = server_socket.accept()
#          client_socket.sendall(cpu_info.encode())
#          client_socket.sendall(host_name.encode())
#          client_socket.sendall(ip_address.encode())
#          client_socket.sendall(platform_info.encode())
