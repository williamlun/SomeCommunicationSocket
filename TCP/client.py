#!/usr/bin/env python3

import sys
from socket import socket, AF_INET, SOCK_DGRAM

SERVER_IP   = '127.0.0.1'
PORT_NUMBER = 5000
SIZE = 1024
print ("Test client sending packets to IP {0}, via port {1}\n".format(SERVER_IP, PORT_NUMBER))

mySocket = socket( AF_INET, SOCK_DGRAM )
myMessage = "Testing12345"
mySocket.sendto(myMessage.encode('utf-8'),(SERVER_IP,PORT_NUMBER))

sys.exit()
