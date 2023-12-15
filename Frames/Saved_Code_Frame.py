import tkinter as tk

import MainVariables
import functions

class SavedCode:
    def __init__(self,frame):
        self.frame = frame

    def SavedCode(self):
        # Scapy Code
        lbl = tk.Label(self.frame,text="Scapy Code",bg=MainVariables.markup_danger,font=('Hack',15,'bold'),width=20)
        lbl.place(x=20,y=30)
        btn = tk.Button(self.frame,text="ICMP" ,bg='blue',font=('Hack',13,'bold'),width=17,bd=0)
        btn.bind("<Button-1>", lambda var: functions.SavedCodeRead("Scapy","ICMP"))
        btn.place(x=45,y=70)
        btn = tk.Button(self.frame,text="ARP" ,bg='blue',font=('Hack',13,'bold'),width=17,bd=0,command=functions.SavedCodeRead)
        btn.bind("<Button-1>", lambda var: functions.SavedCodeRead("Scapy","ARP"))
        btn.place(x=45,y=110)

