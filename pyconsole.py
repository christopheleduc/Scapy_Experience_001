#! /usr/bin/env/ python
# -*- coding: utf-8 -*-
 
 
from platform import python_version
is_version_3 = python_version().startswith( '3' )
 
if is_version_3 :
    from tkinter import Text, StringVar, TclError
else :
    from Tkinter import Text, StringVar, TclError    
 
from subprocess import Popen, PIPE
import re
 
class pyConsole(Text) :
    def __init__( self, master=None, prompt = "> ", width=80, fg='white', bg='black') :
        Text.__init__( self, master, width=width, fg=fg, bg=bg, insertbackground=fg)
        self.prompt = prompt
        self.bind( "<BackSpace>", self.backspace)
        self.bind( "<Key-Return>",self.execute)
        self.bind( "<Key-Left>", self.left)
        self.bind( "<Key-Up>", self.rappelerLigne)
        self.bind( "<Key-Down>", self.rappelerLigne)
        self.bind( "<1>", self.button_1)
        self.bind( "<B1-Motion>", self.button_1)
        self.bind( "<B1-Leave>", lambda event : "break")
        self.bind( "<Double-1>", lambda event : "break") 
        self.bind( "<Triple-1>", lambda event : "break")
        self.bind( "<<Paste>>", self.insert_commande)
        self.insert( "end", self.prompt )
        self.start_commande = '1.0 + %d chars' % len( self.prompt )
        self.lignes = []
        self.numeroligne = 0
 
    def backspace( self, event ) :
        if int( self.index( "insert" ).split(".")[1] ) > len( self.prompt ) :
             self.delete('insert - 1 chars', 'insert')
        return "break"
 
 
    def button_1( self, event ) :
        last_index = self.index( "insert" )
        def testPosition( index ):
            if self.compare( "insert", "<=", "%d.%d" % ( float( self.index( "end" ) ), len( self.prompt ) ) ) :
                self.mark_set( "insert", index )  
        self.after_idle( testPosition, last_index )
 
    def execute( self, event, *args ) :
        commande = self.get()[:-1]
        if self.lignes == [] or self.lignes[-1] != commande and commande != "" :
            self.lignes.append( commande )
            self.numeroligne = len( self.lignes )
        self.insert(END, "\n")
        self.traite(commande)
        self.event_generate('<<command_interpreted>>')
        self.mark_start_commande()
        self.see( "end" )
        self.mark_set( "insert", "end" )
        return "break"
 
    def insert_commande(self, commande) :
        """ A corriger """
        if is_version_3 :
            if type(commande) is not str :
                try :
                    commande = self.clipboard_get()
                except TclError as e :
                    commande = "" 
        else :
            if type(commande) is not unicode :
                try :
                    commande = self.clipboard_get()
                except TclError as e :
                    commande = "" 
        self.insert(END, '\n'+self.prompt+commande+'\n')
        self.traite(commande)
        return "break"
 
    def left( self, event ) :
        if int(self.index("insert").split(".")[1]) <= len(self.prompt) :
            return "break"
 
    def mark_start_commande( self ):
        self.start_commande = self.index('end - 1 chars')
 
 
    def get( self, index1 = None, index2 = None ):
            if index1 is None :
                commande = Text.get(self, self.start_commande, 'end')
                return(commande)
            else :
                return(Text.get(self, index1, index2))
 
    def rappelerLigne(self, event) :
        if self.numeroligne != [] :
            if event.keysym == "Up" :
                self.numeroligne -= 1 
            else :
                self.numeroligne += 1
                
            if self.numeroligne < 0 :
                self.numeroligne = 0
            elif self.numeroligne > len(self.lignes) -1 :
                self.numeroligne = len(self.lignes) -1
            else :
                self.delete("end - 1 line", "end - 1 char")
                self.insert("end", self.prompt + self.lignes[self.numeroligne])                
        return "break"
 
    def traite(self, commande):
        if commande == 'cls' or commande == 'clear': self.clean()
        elif commande.lower == 'exit' or commande == 'quit': self.quit()
        else:
            p = Popen([commande], shell=True, stdout=PIPE, stderr=PIPE)
            output, errors = p.communicate()
            retour = []
            if errors: leretour=errors
            else: leretour=output
            self.insert(END, leretour)
            leretour = leretour.split('\n')
            for elems in leretour:
                retour.append(elems)
            self.insert(END, self.prompt)
            return retour
 
    def clean(self):
        """ Traitement cls/clear """
        self.delete(1.0, END)
        self.insert(END, self.prompt)
 
    def quit(self):
        """ Traitement exit/quit """
        self.destroy()
 
    """ Appels externes """
    def insercmd(self, cmd):
        self.insert(END, '\n'+self.prompt)
        self.insert(END, cmd+'\n')
        retour = self.traite(cmd)
        return retour
 
if __name__ == '__main__' :
    if is_version_3 :
        from tkinter import *
    else :
        from Tkinter import *
 
    def mescommandes():
        reponse1 = pyc.insercmd('python mavar.py')
        print (reponse1)
 
    root = Tk()
    pyc = pyConsole(root)
    pyc.pack()
    Button(root, text='Test', command=mescommandes).pack()
    root.mainloop()