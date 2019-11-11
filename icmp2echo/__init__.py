#!/usr/bin/env python
#coding:utf-8

"""
   Prend un nom ou une adresse IP, envoi un paquet contenat une requete ICMP echo
   et affiche le packet retourné
"""

__version__ = "0.0.1"

from icmp2echo.icmp2echo import icmp2echo