#!/usr/bin/env python
# ig : Interface graphique
#coding:utf-8

# This file is part of a simple Scapy experience with Python3
# See http://www.secdev.org/projects/scapy for more information
# Copyright (C) CryptoDox <cryptodox@cryptodox.net>
# This program is published under a GPLv2 license

__author__ = "Christophe LEDUC"
__date__ =  "02 novembre 2019"

import tkinter as tk
import tkinter.messagebox as tkMessageBox
import os
import sys
from monitor2all import sniffer
from icmp2echo import icmp2echo

"""
   Interface graphique
   Tkinter
"""

__version__ = "0.0.1"


def Reset():
    pass

def On_button():
        
    adresse = value1.get() # adresse IP
    #cidr = self.value2.get() # CIDR
    #data = adresse
    # data = str('192.168.0.1')
    #icmp2echo + data
    tkMessageBox.showinfo('Résultat', message=adresse)
    #icmp2echo(dada)
    button.destroy()

def Icmp2echo():

    #self.value1.set(self.value1)
    adresse = value1.get() # adresse IP
    #self.entree1.pack()
    #adresse = '192.168.0.1'
    print (adresse)
    #cidr = self.value2.get() # CIDR
    # sys.argv = ["./icmp2echo.py", '192.168.0.1']
    sys.argv = ["./icmp2echo.py", adresse]
    exec(open("./icmp2echo.py").read())

    

fenetre = tk.Tk()

fenetre.resizable(True,False)
fenetre.title ("S.E. v0.0.1")

# Label blabla 1
l = tk.LabelFrame(fenetre, text="Scapy Experience v0.0.1", padx=20, pady=20)
l.pack(fill="both", expand="yes")

# Présentation
tk.Label(l, text="Divers cas d'utilisation de Scapy.").pack()

# Copyright
tk.Label(l, text="CryptoDox Copyright 2019.").pack()

# Label Saisie
labelIn1 = tk.LabelFrame(fenetre, text="Saisie", padx=20, pady=20)
labelIn1.pack(fill="both", expand="yes")

# Case à cocher (statistiques)
check_stat = tk.IntVar()
check_stat.set(0)
stat_valide = tk.Checkbutton(labelIn1, text="Afficher les statistiques ?", variable=check_stat, onvalue = 1, offvalue = 0)
stat_valide.pack(side=tk.TOP, padx=10, pady=10)

# Case à cocher (sortie fichier texte)
check_text = tk.IntVar()
check_text.set(0)
texte_valide = tk.Checkbutton(labelIn1, text="Afficher les résultats dans un fichier texte ?", variable=check_text, onvalue = 1, offvalue = 0)
texte_valide.pack(side=tk.TOP, padx=10, pady=10)

# label 1                                             Adresse IP
label1 = tk.Label(labelIn1, text="                    Adresse IP :                    ", bg="green")
label1.pack()

# entrée 1
value1 = tk.StringVar() 
value1.set("Adesse IP V4")
entree1 = tk.Entry(labelIn1, textvariable=value1, width=30)
entree1.pack()

# label 2                                                 CIDR
label2 = tk.Label(labelIn1, text="                        CIDR :                         ", bg="green")
label2.pack()

# entrée 2
value2 = tk.StringVar() 
value2.set("Entrer un CIDR.")
entree2 = tk.Entry(labelIn1, textvariable=value2, width=30)
entree2.pack()

# Label Stats 1
labelStats1 = tk.LabelFrame(fenetre, text="Resultats", padx=20, pady=20)
labelStats1.pack(fill="both", expand="yes")

cadre1 = tk.PanedWindow(labelStats1, orient=tk.VERTICAL)
cadre1.pack(side=tk.TOP, expand=tk.Y, fill=tk.BOTH, pady=2, padx=2)

text_result = tk.Text(cadre1, height='1', font=('Segoe UI', '9'), foreground='green', background='black', wrap=tk.WORD)
text_result.config(state=tk.NORMAL)
text_result.insert('1.0', 'Resultats')
text_result.tag_configure("center", justify='center')
text_result.tag_add("center", 1.0, tk.END)
text_result.config(state=tk.DISABLED)
cadre1.add(text_result)

s1 = tk.Scrollbar(text_result, width=15, cursor='left_ptr') # Test preparation de scrollbar

affiche2 = tk.Label(cadre1, text='Nb d\'entité trouvé !',foreground='green', background='black', anchor=tk.CENTER)
cadre1.add(affiche2)

cadre1.pack()

# Label Actions 1
labelAct1 = tk.LabelFrame(fenetre, text="Actions", padx=20, pady=20)
labelAct1.pack(fill="both", expand="yes")
# bouton de lancer
tk.Button(labelAct1, text="Rechercher", command=Icmp2echo).grid(row=1, column=2)
# bouton de reset
tk.Button(labelAct1, text="  Reset   ", command=Reset).grid(row=1, column=3)
# bouton de sortie
tk.Button(labelAct1, text="  Fermer  ", command=fenetre.destroy).grid(row=1, column=4)

#button = tk.Button(text="Proced!", command=on_button)
#button.pack()
        

fenetre.mainloop()