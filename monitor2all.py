#!/usr/bin/env python
# monitor2all : Monitor all interfaces on a host and print all ARP request
#coding:utf-8

# This file is part of a simple Scapy experience with Python3
# See http://www.secdev.org/projects/scapy for more information
# Copyright (C) CryptoDox <cryptodox@cryptodox.net>
# This program is published under a GPLv2 license

"""
Ecoute constamment toutes les interfaces sur une machine 
et imprime toutes les requêtes ARP qu'elle voit, 
y-compris sur les frames 802.11 d'une carte Wi-Fi en mode moniteur
"""
__author__ = "Christophe LEDUC"
__date__ =  "03 novembre 2019"

from scapy.all import *

def arp_monitor_callback(pkt):
    if ARP in pkt and pkt[ARP].op in (1,2): #who-has or is-at
        return pkt.sprintf("%ARP.hwsrc% %ARP.psrc%")

sniff(prn=arp_monitor_callback, filter="arp", store=0)
