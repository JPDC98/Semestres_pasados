# Save as client.py 
# Message Sender
import os
from socket import *
host = "192.168.0.7" # set to IP address of target computer
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
while True:
    data = input("Enter message to send or type 'exit': ")
    UDPSock.sendto(data.encode('UTF-8'), addr)
    if data == "exit":
        break
UDPSock.close()
os._exit(0)