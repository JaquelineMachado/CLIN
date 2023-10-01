import tkinter
from tkinter import*
from tkinter import Tk, StringVar, ttk
import sqlite3
from tkinter import filedialog as fd
from PIL import Image, ImageTk
import tkinter.messagebox as tkMassageBox
import customtkinter as ctk
import time
import datetime


def prod_serv():
    rootPS = tkinter.Tk()
    rootPS.title("Profissional")
    rootPS.geometry("730x500")
    rootPS.wm_iconbitmap(r'c:\\Users\\User\\Desktop\\Clinica Python\\icone\\icone sistema.ico')

    var = tkinter.StringVar(master = rootPS)

    C = tkinter.Label(rootPS,text="Cadastro de Produto ou Serviço", fg="purple", font="arial 16 bold italic")
    C.place(x=20,y=20)

    l1 = tkinter.Label(rootPS,justify='left',highlightthickness=1,anchor="nw",text="Tipo*?", fg="purple", font="arial 12 bold")
    l1.place(x=20,y=50)
    presr= ctk.CTkOptionMenu(rootPS,width=110,values=["Produto","Serviço"],fg_color="MediumPurple1",button_color="MediumPurple3",button_hover_color="MediumPurple3",dropdown_fg_color="MediumPurple1",dropdown_text_color="Purple")
    presr.place(x=20,y=80)
    
    nps = tkinter.Label(rootPS,justify='left',highlightthickness=1,anchor="nw",text="Nome", fg="purple", font="arial 12 bold")
    nps.place(x=180,y=50)
    nps_1 = tkinter.Entry(rootPS,width=60)
    nps_1.place(x=180,y=80)

    dur = tkinter.Label(rootPS,justify='left',highlightthickness=1,anchor="nw",text="Duração", fg="purple", font="arial 12 bold")
    dur.place(x=20,y=115)
    durac = ctk.CTkOptionMenu(rootPS,width=150,values=["Duração...","30 minutos","40 minutos","50 minutos","1 hora","1 hora e 30 minutos","1 hora e 40 minutos","1 hora e 50 minutos","2 horas"],fg_color="MediumPurple1",button_color="MediumPurple3",button_hover_color="MediumPurple3",dropdown_fg_color="MediumPurple1",dropdown_text_color="Purple")
    durac.place(x=20,y=150)

    ct = tkinter.Label(rootPS,justify='left',highlightthickness=1,anchor="nw",text="Custo (R$)", fg="purple", font="arial 12 bold")
    ct.place(x=20,y=200)
    ct_1 = tkinter.Entry(rootPS,width=20)
    ct_1.place(x=20,y=230)

    pv = tkinter.Label(rootPS,justify='left',highlightthickness=1,anchor="nw",text="Preço venda (R$)", fg="purple", font="arial 12 bold")
    pv.place(x=180,y=200)
    pv_1 = tkinter.Entry(rootPS,width=20)
    pv_1.place(x=180,y=230)

    Date1 = StringVar()
    Date1.set(time.strftime("%d/%m/%Y"))

    lblDate = Label(rootPS,justify='left',highlightthickness=1,anchor="nw",text="Data cadastro", fg="purple", font="arial 12 bold")
    lblDate.place(x=20,y=270)
    Date1= Entry(rootPS,justify='left')
    Date1.place(x=20,y=305)

    slv= Button(rootPS,text="Salvar",fg='purple', width=10,font='Times 12 bold')
    slv.place(x=20,y=350)

    rootPS.mainloop()






