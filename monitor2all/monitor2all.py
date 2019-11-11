#!/usr/bin/env python
# monitor2all : Monitor all interfaces on a host and print all ARP request
#coding:utf-8

# This file is part of a simple Scapy experience with Python3
# See http://www.secdev.org/projects/scapy for more information
# Copyright (C) CryptoDox <cryptodox@cryptodox.net>
# This program is published under a GPLv2 license

__author__ = "Christophe LEDUC"
__date__ =  "03 novembre 2019"

"""
    Implémentation de l'écoute des requêtes ARP

    Usage:

    >>> from monitor2all import sniffer
    >>> sniffer()
"""

from scapy.all import *

__all__ = ['sniffer']

def arp_monitor_callback(pkt):
    if ARP in pkt and pkt[ARP].op in (1,2): #who-has or is-at
        return pkt.sprintf("%ARP.hwsrc% %ARP.psrc%")

def sniffer():
    sniff(prn=arp_monitor_callback, filter="arp", store=0)

if __name__ == '__main__':
    sniffer()
