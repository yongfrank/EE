# 导入 socket、sys 模块
import socket
import sys

# 创建 socket 对象
# serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket = socket.socket()

# 获取本地主机名
host = '0.0.0.0' 

# 设置端口
port = 12345

# 绑定端口
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)

while True:
    # 建立客户端连接
    clientsocket, addr = serversocket.accept()
    
    print(f"连接地址：{addr}") 
    
    while True:
        print(clientsocket.recv(1024))
        # msg = '欢迎访问菜鸟教程！' + "\r\n"
        # clientsocket.send(msg.encode('utf-8'))
        clientsocket.send(b'Welcome to connect the server!')
    
    clientsocket.close()
