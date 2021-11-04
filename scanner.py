import sys #buat ngetik cmd commands
import socket
from datetime import datetime

#targetnya
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #ganti host name --> IPv4
else:
    print("Argumen salah.")
    print("syntax: python3 scanner.py <ip>")
    sys.exit()
    
#banner biar bagus
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
    print("\nKeluar. ")
    sys.exit()
    
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()
    
except socket.error:
    print("Couldn't connect to server.")
    sys.exit()

#scanner.py by tyagapn02
#on THM
#MD5 = 02d5b23d19c8ca94a761fcb21e37408c
#for bro J