#! /usr/bin/env/ python
# -*- coding: utf-8 -*-

# from tkinter import *
# from tkinter.messagebox import * # boîte de dialogue
import tkinter as tk
import tkinter.messagebox as tkMessageBox
import os
import sys

def Verification():
    if Motdepasse.get() == 'python27':
        # le mot de passe est bon : on affiche une boîte de dialogue puis on ferme la fenêtre
        tkMessageBox.showinfo('Résultat','Mot de passe correct.\nAu revoir !')
        Mafenetre.destroy()
    else:
        # le mot de passe est incorrect : on affiche une boîte de dialogue
        tkMessageBox.showwarning('Résultat','Mot de passe incorrect.\nVeuillez recommencer !')
        #tkMessageBox.showinfo(message=Motdepasse.get())
        Motdepasse.set('')

# Création de la fenêtre principale (main window)
Mafenetre = tk.Tk()
Mafenetre.title('Identification requise')

# Création d'un widget Label (texte 'Mot de passe')
Label1 = tk.Label(Mafenetre, text = 'Mot de passe ')
Label1.pack(side = tk.LEFT, padx = 5, pady = 5)

# Création d'un widget Entry (champ de saisie)
Motdepasse= tk.StringVar()
Champ = tk.Entry(Mafenetre, textvariable= Motdepasse, show='*', bg ='bisque', fg='maroon')
Champ.focus_set()
Champ.pack(side = tk.LEFT, padx = 5, pady = 5)

# Création d'un widget Button (bouton Valider)
Bouton = tk.Button(Mafenetre, text ='Valider', command = Verification)
Bouton.pack(side = tk.LEFT, padx = 5, pady = 5)

Mafenetre.mainloop()