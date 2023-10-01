import tkinter
from window2 import menu
import tkinter.messagebox as tkMassageBox
from tkinter import *
from tkinter.ttk import *
import sqlite3
import customtkinter as ctk


root=None
userbox=None
passbox=None
topframe=None
bottomframe=None
frame3=None
login=None

def GET():
   global userbox,passbox,error
   J1 = userbox.get()
   J2 = passbox.get()

   if (J1=='Jack1' and J2=='123'):
        menu()
   elif (J1=='Jack2' and J2=='123'):
        menu()
   else:
      error=tkinter.Label(bottomframe,text="Usuário ou senha inválido.", fg="red", font="bold")
      error.pack()
def Entry():
    global userbox,passbox,login,topframe,bottomframe,image_1
    root = tkinter.Tk()
    root.geometry("400x500")
    topframe = tkinter.Frame(root)
    topframe.pack()
    
    bottomframe = tkinter.Frame(root)
    bottomframe.pack()

    heading = tkinter.Label(topframe,text ="Autenticação", fg='purple', font='Times 20 bold italic')
    heading.place(y=10)
   
    username = tkinter.Label(topframe,width=50,justify='left',highlightthickness=1, text ="Usuário :", anchor="nw",fg='purple', font='Times 14')
    userbox = tkinter.Entry(topframe, width=40,justify='left',highlightthickness=1,font='Times 14')

    password = tkinter.Label(bottomframe,width=50,justify='left',highlightthickness=1, text ="Senha :", anchor="nw", fg='purple', font='Times 14')
    passbox = tkinter.Entry(bottomframe, width=40,justify='left',highlightthickness=1, show='*',font='Times 14')
    
    login = tkinter.Button(bottomframe, width=20,text="LOGIN", font='Ivy 12 bold',fg='purple', command=GET)
    

    root.wm_iconbitmap(r'c:\\Users\\User\\Desktop\\Clinica Python\\icone\\icone sistema.ico')
    image= tkinter.PhotoImage(file =r"c:\\Users\\User\\Desktop\\Clinica Python\\Imagem\\imagg.png")
    image=image.subsample(1,1)
    labelimg=tkinter.Label(image=image, height="250", width="250")
    labelimg.pack()

    heading.pack()
    username.pack()
    userbox.pack()
    password.pack()
    passbox.pack()
    login.pack()
    root.title("Sistema Clínica")
    root.mainloop()

    '''if login==login:
       root.hide()'''

Entry()



