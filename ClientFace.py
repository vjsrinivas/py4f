__author__ = 'Vijaysrinivas Rajagopal'

from RCONBase import TCPBARE
from Kommands import *
import socket
from Chatter import *
from PlayerFace import *

#Dependencies
ip = "00.000.000.000"
port = 0000
buffer = 9999
password = ""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
