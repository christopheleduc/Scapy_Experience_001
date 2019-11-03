#!/usr/bin/env python
#coding:utf-8

# This file is part of a simple Scapy experience with Python3
# See http://www.secdev.org/projects/scapy for more information
# Copyright (C) CryptoDox <cryptodox@cryptodox.net>
# This program is published under a GPLv2 license

"""
   Divers cas d'utilisation
   de Scapy
"""
__author__ = "Christophe LEDUC"
__date__ =  "02 novembre 2019"

# %matplotlib inline
# import matplotlib.pyplot
# %matplotlib inline

#import sys
from scapy.all import *
from scapy.utils import *
import matplotlib

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