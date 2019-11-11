#!/usr/bin/env python
# main : main
#coding:utf-8

# This file is part of a simple Scapy experience with Python3
# See http://www.secdev.org/projects/scapy for more information
# Copyright (C) CryptoDox <cryptodox@cryptodox.net>
# This program is published under a GPLv2 license

__author__ = "Christophe LEDUC"
__date__ =  "02 novembre 2019"

# %matplotlib inline
# import matplotlib.pyplot
# %matplotlib inline

#import sys
from scapy.all import *
from scapy.utils import *
import matplotlib

"""
   Divers cas d'utilisation
   de Scapy
"""

__version__ = "0.0.1"

packet = IP()
print (packet.show())

packet1 = IP(dst='192.168.0.254')
packet1.ttl = 42
print (packet1.show())

packet2 = IP(dst='192.168.0.254')/ICMP()
print (packet2.show2())

# packet3=IP(dst='192.168.0.254')/ICMP()/Raw(load=RandString(56))

# reponse = sr1(packet3, timeout=1)
# print (reponse.show())

# pcap = rdpcap('sniffed_packets.pcap')
# s = pcap.sessions()

# for key, value in s.iteritems():

#      # Looking for telnet sessions
#      if ':23' in key:
#          for v in value:
#              try:
#                  v.getlayer(Raw).load
#              except AttributeError:
#                  pass

ans, unans = srloop(IP(dst=["8.8.8.8", "8.8.4.4"])/ICMP(), inter=.1, timeout=.1, count=100, verbose=False)
#%matplotlib inline
ans.multiplot(lambda x, y: (y[IP].src, (y.time, y[IP].id)), plot_xy=True)

pkt = IP() / UDP() / DNS(qd=DNSQR())
print(repr(raw(pkt)))



ans = sr([IP(dst="8.8.8.8", ttl=(1, 8), options=IPOption_RR())/ICMP(seq=RandShort()), IP(dst="8.8.8.8", ttl=(1, 8), options=IPOption_Traceroute())/ICMP(seq=RandShort()), IP(dst="8.8.8.8", ttl=(1, 8))/ICMP(seq=RandShort())], verbose=False, timeout=3)[0]
ans.make_table(lambda x, y: (", ".join(z.summary() for z in x[IP].options) or '-', x[IP].ttl, y.sprintf("%IP.src% %ICMP.type%")))


print("********************************************************************************")
packet_new01 = Ether()/IP(dst="www.secdev.org")/TCP()
packet_new01.summary()

print(packet_new01.dst)  # first layer that has an src field, here Ether
print(packet_new01[IP].src)  # explicitly access the src field of the IP layer

# sprintf() is a useful method to display fields
print(packet_new01.sprintf("%Ether.src% > %Ether.dst%\n%IP.src% > %IP.dst%"))

print(packet_new01.sprintf("%TCP.flags% %TCP.dport%"))

# [p for p in IP(ttl=(1,5))/ICMP()]