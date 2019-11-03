#! /usr/bin/env python
# arping2tex : arpings a network and outputs a LaTeX table as a result
#coding:utf-8

# This file is part of a simple Scapy experience with Python3
# See http://www.secdev.org/projects/scapy for more information
# Copyright (C) CryptoDox <cryptodox@cryptodox.net>
# This program is published under a GPLv2 license

"""
Le moyen le plus rapide pour découvrir un asset
sur un réseau local ethernet est d'utiliser la méthode ARP ping

Le formatage LaTex n'est pas disponible sous zindows
"""
__author__ = "Christophe LEDUC"
__date__ =  "03 novembre 2019"

import sys
if len(sys.argv) != 2:
    print ("Usage: arping2tex <net>\n  eg: arping2tex 192.168.1.0/24")
    sys.exit(1)

from scapy.all import srp,Ether,ARP,conf
conf.verb=0
ans,unans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=sys.argv[1]),
              timeout=2)

print (r"\begin{tabular}{|l|l|}")
print (r"\hline")
print (r"MAC & IP\\")
print (r"\hline")
for snd,rcv in ans:
    print (rcv.sprintf(r"%Ether.src% & %ARP.psrc%\\"))
print (r"\hline")
print (r"\end{tabular}")