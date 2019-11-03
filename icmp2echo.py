#!/usr/bin/env python
# icmp2echo : take IP or name to send ICMP echo request packet and displays the return packet
#coding:utf-8

# This file is part of a simple Scapy experience with Python3
# See http://www.secdev.org/projects/scapy for more information
# Copyright (C) CryptoDox <cryptodox@cryptodox.net>
# This program is published under a GPLv2 license

"""
   Prend un nom ou une adresse IP, envoi un paquet contenat une requete ICMP echo
   et affiche le packet retourné
"""
__author__ = "Christophe LEDUC"
__date__ =  "03 novembre 2019"

import sys
if len(sys.argv) != 2:
    print ("Usage: icmp2echo <IP or hostname>\n  eg: icmp2echo 192.168.1.1")
    sys.exit(1)

from scapy.all import sr1, IP, ICMP

packet = sr1(IP(dst=sys.argv[1])/ICMP())
if packet:
    packet.show()