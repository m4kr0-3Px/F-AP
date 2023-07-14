import re,sys,time
from scapy.all import *
from scapy.layers.dot11 import *


def our_broadcast():
    ssid = input("Enter the SSID name: ")
    iface = input("Enter the interface who activated monitor mode: ")

    sender = RandMAC()

    dot11 = Dot11(type=0, subtype=8, addr1="ff:ff:ff:ff:ff:ff", addr2=sender, addr3=sender)
    beacon = Dot11Beacon()

    setting = Dot11Elt(ID="SSID", info=ssid, len=len(ssid))

    final = RadioTap() / dot11 / beacon / setting

    sendp(final, inter=0.01, iface=iface, loop=1)



text_2=subprocess.check_output(["iwconfig"]).decode("utf-8")


regex_1 = r'Mode:Monitor'
regex_2=r'Mode:Managed'

matches=re.search(regex_1, str(text_2))
matches_2=re.search(regex_2,str(text_2))


if matches:
    our_broadcast()
elif matches_2:
    print("Please change the interface's mode to Monitor Mode")
    choose=int(input("1-I can change\n2-Please do it\nChoice: "))
    if choose==1:
        print("Sure,I'm waiting here...")
        sys.exit()
    elif choose==2:
        print("Okeeeeyy,I'm starting please wait...");time.sleep(0.5)
        iface_name=input("Please Enter Your interface name(eht0,wlan0,etc.): ")
        result = subprocess.run(['airmon-ng', 'start',f'{iface_name}'], capture_output=True, text=True)
        if result:
            print("I changed,you can continue my friend:)\n")
            our_broadcast()
else:
    print("I guess your wifi adapter is not active :)");sys.exit()





















