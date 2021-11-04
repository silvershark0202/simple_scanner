#!/bin/python
import sys
import socket
from datetime import datetime


if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Argumen salah.")
    print("syntax: python3 scanner.py <ip>")
    sys.exit()
    

print("-" * 50)
print(f"scanning target {target}")
print("time : " + str(datetime.now()))
print("-" * 50)

try:
    for port in range(50, 85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) #is a float
        result = s.connect_ex((target,port))
        print("checking port {}".format(port))
        if result == 0:
            print("port {} terbuka".format(port))
        s.close()
        
except KeyboardInterrupt:
    print("\nexit. ")
    sys.exit()
    
except socket.gaierror:
    print("Hostname error.")
    sys.exit()
    
except socket.error:
    print("Cannot connect to server")
    sys.exit()
