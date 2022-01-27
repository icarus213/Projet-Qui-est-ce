from tkinter import *
import tkinter as tk


import recup

recup.test()
win= Tk()
win.title("Qui est-ce ?")
win.geometry("750x550") 
win.minsize(700,500)
win.iconphoto(True, tk.PhotoImage("images/logo.jpg"))
win.config(background='grey')


label_title = Label(win, text="C KI ?",font=("Courrier",40), bg='grey')
label_title.pack()


def destroy_window():
  win.destroy()
  
def new_window():
  win2= Tk()
  win2.geometry("750x550")
  win.destroy()

Start_Button = Button(win, text= "Play", font=("Courrier",20), bg='white',command=new_window)

Leave_Button = Button(win, text= "Leave", font=("Courrier",20),bg='white',command=destroy_window)

Start_Button.pack(pady=25)
Leave_Button.pack(pady=25)
win.mainloop()

