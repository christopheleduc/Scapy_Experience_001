#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Ce module ecoute constamment toutes les interfaces sur une machine 
et imprime toutes les requêtes ARP qu'elle voit, 
y-compris sur les frames 802.11 d'une carte Wi-Fi en mode moniteur
"""

__version__ = "0.0.1"

from monitor2all.monitor2all import arp_monitor_callback, sniffer