__author__ = 'Vijaysrinivas Rajagopal'

import socket
from Kommands import *
from Chatter import *
from PlayerFace import *
import threading
import time


#Dependencies
ip = ""
port = 0000
buffer = 100000
password = ""

# Create main socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Create a variable to handle the connection mumbo gumbo
handler = TCPBARE(ip, port, buffer, password, s)
#Actually connect and auth
handler.connect()
handler.auth()
kommander = BF2CC(s)
chatterina = ChatLog()

#while True:
    #chatterina.writelog(kommander.getchatresponse("Admin"))
    #time.sleep(1)

handler.close()
