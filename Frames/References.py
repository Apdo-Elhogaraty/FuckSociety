import os
import tkinter as tk
import MainVariables
import functions

class Reference:
    def __init__(self,frame):
        self.frame = frame
    def Reference(self):
        #================== Books
        books_lbl = tk.Label(self.frame,text="Books",bg=MainVariables.markup_danger,fg="#fff",font=('Hack',15,'bold'),width=23)
        books_lbl.place(x=20,y=30)
        #-- Black Hat Python
        btn = tk.Button(self.frame, text="Black Hat Python", bg='#44bd32', fg="#000",font=('Hack', 13, 'bold'), width=25)
        btn.bind("<Button-1>", lambda x:functions.Refrances("Black_Hat_Python.pdf","Books"))
        btn.place(x=20, y=70)
        #-- Linux Commands Handbook
        btn = tk.Button(self.frame, text="Linux Commands Handbook", bg='#44bd32', fg="#000",font=('Hack', 13, 'bold'), width=25)
        btn.bind("<Button-1>", lambda x:functions.Refrances("linux-commands-handbook.pdf","Books"))
        btn.place(x=20, y=120)
        #-- Linux Basics For Hackers
        btn = tk.Button(self.frame, text="Linux Basics For Hackers", bg='#44bd32', fg="#000",font=('Hack', 13, 'bold'), width=25)
        btn.bind("<Button-1>", lambda x:functions.Refrances("linux_basics_for_hackers.pdf","Books"))
        btn.place(x=20, y=170)
        #-- Operating System Concepts
        btn = tk.Button(self.frame, text="Operating System Concepts", bg='#44bd32', fg="#000",font=('Hack', 13, 'bold'), width=25)
        btn.bind("<Button-1>", lambda x:functions.Refrances("Operating\\ System\\ Concepts.pdf","Books"))
        btn.place(x=20, y=220)
        # -- The Hacker Playbook 2
        btn = tk.Button(self.frame, text="The Hacker Playbook 2", bg='#44bd32', fg="#000",font=('Hack', 13, 'bold'), width=25)
        btn.bind("<Button-1>", lambda x:functions.Refrances("The\\ Hacker\\ Playbook\\ 2.pdf","Books"))
        btn.place(x=20, y=270)
        #============ eJPTv1
        lbl = tk.Label(self.frame,text="eJPTv1",bg=MainVariables.markup_danger,fg="#fff",font=('Hack',15,'bold'),width=20)
        lbl.place(x=350,y=30)
        btn = tk.Button(self.frame,text="eJPTv1 Slides",bg='#353b48', fg="#000",font=('Hack', 13, 'bold'), width=22)
        btn.bind("<Button-1>", lambda x:functions.Refrances(name="ejpt\\ Slides"))
        btn.place(x=350,y=70)
        #============ Operating Systems
        lbl = tk.Label(self.frame,text="Operating Systems",bg=MainVariables.markup_danger,fg="#fff",font=('Hack',15,'bold'),width=20)
        lbl.place(x=350,y=130)
        btn = tk.Button(self.frame,text="OS Slides",bg='#353b48', fg="#000",font=('Hack', 13, 'bold'), width=22)
        btn.bind("<Button-1>", lambda x:functions.Refrances(name="Operating\\ Systems"))
        btn.place(x=350,y=170)
        #============ Network
        lbl = tk.Label(self.frame,text="Network",bg=MainVariables.markup_danger,fg="#fff",font=('Hack',15,'bold'),width=20)
        lbl.place(x=350,y=230)
        btn = tk.Button(self.frame,text="Nmap Sheet",bg='#273c75', fg="#000",font=('Hack', 13, 'bold'), width=22)
        btn.bind("<Button-1>", lambda x:functions.Refrances(name="Nmap-Cheat-Sheet.pdf"))
        btn.place(x=350,y=270)
        btn = tk.Button(self.frame,text="CCNA 200-125",bg='#273c75', fg="#000",font=('Hack', 13, 'bold'), width=22)
        btn.bind("<Button-1>", lambda x:functions.Refrances(name="ccna.pdf"))
        btn.place(x=350,y=320)

