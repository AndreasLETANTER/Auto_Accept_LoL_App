from enum import auto
import pyautogui
import time
import sys
from tkinter import *
from auto_accept import control_center
from github import open_github

######################CONFIG######################

window = Tk()

window.title("Auto Accept")
window.geometry("800x600")
window.minsize(800, 600)
window.maxsize(800, 600)
window.iconbitmap("app_resources/logo_riot.ico")
window.config(background='#4065A4')

######################FUNCTIONS######################

def task():
    global after_id
    control_center(ban_entry.get(), pick_entry.get())
    log_file = open("log.log", "r")
    log.insert(END, log_file.read())
    after_id = window.after(2000, task)

def switch():
    global after_id
    if start_button.config('text')[-1] == 'Start':
        start_button.config(text='Stop')
        window.update()
        task()
    else:
        start_button.config(text='Start')
        window.update()
        window.after_cancel(after_id)
        after_id = None

######################FRAME######################

frame_text = Frame(window, bg='#4065A4')
frame_button = Frame(window, bg='#4065A4')
frame_entry = Frame(window, bg='#4065A4')
frame_pick_ban = Frame(window, bg='#4065A4')

######################TEXT######################

label_title = Label(frame_text, text="Welcome to the Auto Accept application", font=("Helvetica", 20), bg='#4065A4', fg='white')
label_sub_title = Label(frame_text, text="Made in Python by Andréas LE TANTER", font=("Helvetica", 15), bg='#4065A4', fg='white')
pick_entry = Entry(frame_entry, font=("Helvetica", 20), bg='#4065A4', fg='white', width=21)
ban_entry = Entry(frame_entry, font=("Helvetica", 20), bg='#4065A4', fg='white', width=21)
ban_text = Label(frame_pick_ban, text="Ban :", font=("Helvetica", 15), bg='#4065A4', fg='white')
pick_text = Label(frame_pick_ban, text="Pick :", font=("Helvetica", 15), bg='#4065A4', fg='white')
log = Text(window, height = 5, width = 52, font=("Helvetica", 15), bg='#4065A4', fg='white')

######################BUTTON######################

start_button = Button(frame_button, text="Start", font=("Courrier", 15), bg='white', fg='#4065A4', width=30, command=switch)
git_button = Button(frame_button, text="GitHub", font=("Courrier", 15), bg='white', fg='#4065A4', command=open_github)

######################PACK######################

label_title.pack()
label_sub_title.pack()
ban_entry.pack()
pick_entry.pack()
start_button.pack(fill=X)
git_button.pack(fill=X)
frame_text.pack()
frame_button.pack(pady=25)
ban_text.pack(pady=10)
pick_text.pack()
log.pack()

######################PLACE######################

frame_text.place(in_=window, anchor="c", relx=.5, rely=.3)
frame_entry.place(in_=window, anchor="c", relx=.547, rely=.47)
frame_button.place(in_=window, anchor="c", relx=.5, rely=.63)
frame_pick_ban.place(in_=window, anchor="c", relx=.25, rely=.46)
log.place(in_=window, anchor="c", relx=.5, rely=.85)

######################START######################

window.mainloop()