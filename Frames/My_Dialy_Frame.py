import tkinter as tk
import datetime
import MainVariables
import functions
import requests
from bs4 import BeautifulSoup
import webbrowser

class MyDiary:
    def __init__(self,frame):
        self.frame = frame
    def MyDiary(self):
        lbl = tk.Label(self.frame,text="Enter Your Routine For Today :",bg=MainVariables.markup_yellow,font=('Hack',15,'underline'))
        lbl.place(x=15,y=20)
        txt_area = tk.Text(self.frame,width=30,height=10 ,font=('Hack',15,''))
        txt_area.insert(tk.END,functions.DialyRead())
        txt_area.place(x=400,y=20)
        btn = tk.Button(self.frame,text="Virus",bg=MainVariables.virus_btn_bg,font=('Hack',15,'bold'))
        btn.bind("<Button-1>",lambda e: functions.DialyWrite(txt_area.get("1.0",tk.END)))
        btn.bind("<Enter>", lambda a: btn.configure(
            cursor="target"
        ))

        btn.place(x=680,y=270)

        # --- Hacker News Section ---
        lbl = tk.Label(self.frame,text="The Hacker News Today :",bg=MainVariables.markup_danger,font=('Hack',15,'underline'))
        lbl.place(x=15,y=320)
        self.HackerNews()

        # --- Problem Solving News Section ---
        lbl = tk.Label(self.frame,text="challenge Your Self In Problem Sovling Task :",bg=MainVariables.markup_yellow,font=('Hack',15,'underline'))
        lbl.place(x=15,y=600)
        btn = tk.Button(self.frame,text="Hacker Ranke" ,bg=MainVariables.main_frame_bg,font=('Hack',12,''),bd=0,fg='#fff')
        btn.bind("<Button-1>",lambda e: webbrowser.open_new("https://www.hackerrank.com/domains/python?filters[status][]=unsolved&badge_type=python"))
        btn.bind("<Enter>", lambda a: btn.configure(
            cursor="target"
        ))
        btn.place(x=570,y=598)

    def HackerNews(self):
        try:
            request = requests.get("https://thehackernews.com/")
            soup = BeautifulSoup(request.text,"html.parser")
            list = soup.find_all(class_="body-post")
            DateNow = datetime.datetime.now().day
            DateNow = "0" + str(DateNow) if DateNow < 10 else str(DateNow)
            place_Y = 320
            # counter => site get 10 posts if thare are no one today show Text
            counter = 0

            for post in list:
                Date = post.select("span.h-datetime")[0].text.strip()[5:7]
                if Date == DateNow:
                    link = post.a["href"]
                    postTitle = post.h2.text.strip()
                    lbl = tk.Label(self.frame, text=str(list.index(post)+1)+"- "+postTitle, bg=MainVariables.main_frame_bg,
                                   fg='#fff',font=('Hack', 13, 'underline'))

                    # Function To correct loop by use bind
                    def make_link(x):
                        return lambda ev: webbrowser.open_new(x)
                    lbl.bind("<Button-1>", make_link(link))
                    lbl.place(x=80, y=place_Y+40)
                    place_Y+=40
                else:
                    counter+=1
            if counter == 10:
                lbl = tk.Label(self.frame, text="Sorry, No Hacker News Today ^.^ ...!",
                               bg=MainVariables.main_frame_bg,
                               fg='#fff', font=('Hack', 13, 'underline'))
                lbl.place(x=300, y=400)
        except:
            lbl = tk.Label(self.frame, text="InterNet Faild To Connection ^.^ ...!",
                           bg=MainVariables.main_frame_bg,
                           fg='#fff', font=('Hack', 13, 'underline'))
            lbl.place(x=300, y=400)
            print("InterNet Faild To Connection ...")



