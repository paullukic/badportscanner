#!bin/python3

import sys
import socket
from datetime import datetime

# define target
if len(sys.argv) == 2:

	#transform hostname to IPv4
	target = socket.gethostbyname(sys.argv[1])
	
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")
	
# create console drawing
print("-" * 50)
print("Scanning target " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

try:
	for port in range(50, 85):

		# socket.AF_INET is IPv4 and socket.SOCK_STREAM is port
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)

		# connect to our target and loop thro port range
		result = s.connect_ex((target, port))
		
		# if port is open it will return 0
		# if port is not open it will return 1
		if result == 0:
			print("Port {} is open".format(port))
		s.close()

# if you do ctrl+c exits from py script		
except KeyboardInterrupt:
	print("\nStopping script.")
	sys.exit()

# if you cannot get the host name
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

# if you cant connect to the IP target
except socket.error:
	print("Couldn't connect to server.")
	sys.exit()
