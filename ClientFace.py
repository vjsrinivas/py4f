__author__ = 'Vijaysrinivas Rajagopal'

from RCONBase import TCPBARE
from Kommands import *
import socket
from Chatter import *

#Dependencies
ip = "00.000.000.000"
port = 0000
buffer = 0000
password = ""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
