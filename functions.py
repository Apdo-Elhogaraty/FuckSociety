import datetime
import tkinter as tk
import os
from tkinter import filedialog
import MainVariables


# ========== Structure Page ======
# Select Dialy Frame
# Select savedCode Frame
# DialyWrite
# DialyRead
#Saved Code Read
# =================================
# ---- Select Dialy Frame ----
def Diary(*frameList):
    for frame in frameList:
        if str(frame) == '.!frame2':
            frame.place(x=301, y=0, width=1066, height=768)
        else:
            frame.place_forget()

# ---- Select References Frame ----
def savedCode(*frameList):
    for frame in frameList:
        # frame.place_forget()
        if str(frame) == '.!frame3':
            frame.place(x=301, y=0, width=1066, height=768)
        else:
            frame.place_forget()

# ---- References Frame ----
def Reference(*frameList):
    for frame in frameList:
        # frame.place_forget()
        if str(frame) == '.!frame4':
            frame.place(x=301, y=0, width=1066, height=768)
        else:
            frame.place_forget()

# ---- DialyWrite ----
def DialyWrite(myDialy):
    dialy = open(f"{MainVariables.project_path}/Data/Diary/" + str(datetime.datetime.now().date()),"w")
    dialy.write(myDialy)
    dialy.close()

# ---- DialyRead ----
def DialyRead():
    directory = f"{MainVariables.project_path}/Data/Diary"
    for file in os.listdir(directory):
        if str(datetime.datetime.now().date()) == file:
            daily = open(f"{MainVariables.project_path}/Data/Diary/"+ str(datetime.datetime.now().date()),"r")
            return daily.read()

    return """Enter Your Malicious Routine!:
------------------------------"""
# ---- Saved Code Read ----
def SavedCodeRead(section,name):
        path = f"{MainVariables.project_path}/Data/SavedCode/{section}/{name}.py"
        os.system(f"xdg-open {path}")


# ---- References ----
def Refrances(name,infolder="no"):
    path = MainVariables.project_path+"/Data/References/"
    if infolder == "no":
        path =path+name
        os.system(f"xdg-open {path}")
    else :
        path =path+infolder+"/"+name
        os.system(f"xdg-open {path}")

# ================ Old Code ==========
# def SavedCodeRead(section,name):
    # def saveFile():
    #     files = [('All Files', '*.*'),
    #              ('Python Files', '*.py'),
    #              ('Text Document', '*.txt')]
    #     file = filedialog.asksaveasfile(filetypes=files, defaultextension=".py")
    # window = tk.Tk()
    # window.title(f"{name} Code")
    # window.geometry("800x600")
    # btn = tk.Button(window, text='Click to Save File',command= lambda : saveFile()).pack(fill=tk.X)
    # directory = f"{MainVariables.project_path}/Data/SavedCode/{section}/"
    # for file in os.listdir(directory):
    #     if file == name+".py":
    #         f = open(f"{directory}{file}","r")
    #         txt = tk.Text(window, font=('Hack', 13, 'bold'))
    #         txt.insert(tk.END, f.read())
    #         break
    #     else:
    #         txt = tk.Text(window,font=('Hack',13,'bold'))

    # txt.pack()
    # window.mainloop()
