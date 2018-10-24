import os
import time 

blue = '\033[34;1m'
green = '\033[32;1m'
purle = '\033[35;1m'
cyan = '\033[36;1m'
red = '\033[31;1m'
white = '\033[37;1m'
yellow = '\033[33;1m'

print (red),("[1]Hack CCTV")
print (yellow),("[2]B4J164Nv5")
print (green),("[3]MBF (Multi Brute Force)")
print (blue),("Script Created By:")
print (blue),("Mr.J106")
print (cyan)
p = input("Pilih No: ")

if p == 1:
    while True:
        try:
            os.system ('pkg install figlet')
            os.system ('clear')
            os.system ('figlet "J106"')
            os.system ('apt update && apt upgrade -y')
            os.system ('pkg install git -y')
            os.system ('pkg install python2 -y')
            os.system ('pip2 install requests -y')
            os.system ('git clone https:github.com/kancotdiq/ipcs')
        print (red),("Jalankan Dengan Perintah: ")
        time.sleep (1.4)
        print (blue),("cd ipcs")
        time.sleep (1.4)
        print (blue),("python2 scan.py")
        print (green),("-----------------B")
        time.sleep (1.0)