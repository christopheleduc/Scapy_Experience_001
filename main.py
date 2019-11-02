import sys
from scapy.all import sr1, IP, ICMP

packet = IP()
print (packet.show())