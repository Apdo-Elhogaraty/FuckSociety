#!/usr/bin/python3
import random
import shutil
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import functions
import MainVariables
from Frames import My_Dialy_Frame,Saved_Code_Frame,References
import sys
sys.tracebacklimit = 0

class App:
    def __init__(self,root):
# ---Program Configration
        root.geometry("1366x768")
        root.minsize(width=1100,height=600)
        root.title('Fuck Society')
        root.configure(bg=MainVariables.program_bg)
#--- Main Home ---
        # --- Home Frame ---
        homeFrame = tk.Frame(root)
        homeFrame.place(x=302, y=0,width=1066,height=768)

# --- main window background image ---
#         img = Image.open(f"{MainVariables.project_path}/images/{random.randrange(1, 12, 1)}.jpg")
        img = Image.open(f"{MainVariables.project_path}/images/{random.randrange(1, 14, 1)}.jpg")
        image1 = img.resize((1066, 768))
        test = ImageTk.PhotoImage(image1)
        label1 = tk.Label(homeFrame,image=test,bd=0)
        label1.image = test
        label1.place(x=0, y=0)
        # Dialy Frame
        diaryFrame = tk.Frame(root,bg=MainVariables.main_frame_bg)
        Frame_Class = My_Dialy_Frame.MyDiary(diaryFrame)
        Frame_Class.MyDiary()
        # Saved Code Frame
        codeFrame = tk.Frame(root, bg=MainVariables.main_frame_bg)
        Frame_Class = Saved_Code_Frame.SavedCode(codeFrame)
        Frame_Class.SavedCode()
        # References Frame
        Reference_Frame = tk.Frame(root, bg=MainVariables.main_frame_bg)
        Reference_Class = References.Reference(Reference_Frame)
        Reference_Class.Reference()

# --- Frame List ---
        frameList = [homeFrame,diaryFrame,codeFrame,Reference_Frame]
        # print(str(frameList[2]))
# --- SideBar ---
        # --- SideBar Frame ---
        sideBar = tk.Frame(root, bg=MainVariables.sidebar_bg)
        sideBar.place(x=0, y=0, width=300, height=768)
        # --- SideBar Top Image ---
        img = Image.open(f"{MainVariables.project_path}/images/SideBar.png")
        image = img.resize((200, 200))
        photo = ImageTk.PhotoImage(image)
        lbl = tk.Label(sideBar, image=photo, bd=0,bg='#000')
        lbl.image = photo
        lbl.place(x=25, y=20)
        # ------------------------- Buttons ----------------------
        btn1 = tk.Button(sideBar, text='My Diary', width=17,bg=MainVariables.btn_bg,fg='#000',bd=0,font=('Hack',15,'bold'))
        btn1.bind("<Button-1>", lambda var: functions.Diary(*frameList))
        btn1.place(x=35,y=250)
        btn2 = tk.Button(sideBar, text='Saved Code', width=17, bg=MainVariables.btn_bg, fg='#000', bd=0, font=('Hack', 15, 'bold'))
        btn2.bind("<Button-1>", lambda var: functions.savedCode(*frameList))
        btn2.place(x=35, y=300)
        btn3 = tk.Button(sideBar, text='References', width=17, bg=MainVariables.btn_bg, fg='#000', bd=0, font=('Hack', 15, 'bold'))
        btn3.bind("<Button-1>", lambda var: functions.Reference(*frameList))
        btn3.place(x=35, y=350)
        # btn4 = tk.Button(sideBar, text='Tools', width=17, bg=MainVariables.btn_bg, fg='#000', bd=0, font=('Hack', 15, 'bold'))
        # btn4.bind("<Button-1>", lambda var: functions.Reference(*frameList))
        # btn4.place(x=35, y=400)
        btn5 = tk.Button(sideBar, text='Virus', width=17, bg=MainVariables.virus_btn_bg, fg='#fff', bd=0, font=('Hack', 15, 'bold'),command=root.quit)
        btn5.place(x=35, y=600)
        btn5.bind("<Enter>", lambda a: btn5.configure(
                cursor="target"
        ))

# try:
#         root = tk.Tk()
#         myApp = App(root)
#         root.mainloop()
#         shutil.rmtree(root)
# except Exception:
#     pass

root = tk.Tk()
myApp = App(root)
root.mainloop()