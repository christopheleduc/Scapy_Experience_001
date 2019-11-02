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

import sys
from scapy.all import sr1, IP, ICMP

packet = IP()
print (packet.show())