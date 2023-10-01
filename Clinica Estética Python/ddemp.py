import tkinter
from tkinter.ttk import *
from tkinter import *
import sqlite3
import customtkinter as ctk
from tkinter import Tk, StringVar, ttk
from tkcalendar import Calendar, DateEntry
from formasdepg import fpg
import pygame, sys, random


def dd_emp():
    pygame.init()
    rootdemp = tkinter.Tk()
    rootdemp.geometry("965x670")
    rootdemp.title("Sistema Clínica")
    rootdemp.wm_iconbitmap(r'c:\\Users\\User\\Desktop\\Clinica Python\\icone\\icone sistema.ico')
    
    frameCima = Frame(rootdemp,width=960,height=350,relief=FLAT)
    frameCima.grid(row=0,column=0,pady=0,padx=0,sticky=NSEW)

    frameBaixo = Frame(rootdemp,width=960,height=260,bg='MediumPurple1',pady=20,bd= 10,relief=RIDGE)
    frameBaixo.grid(row=2,column=0,pady=0,padx=1,sticky=NSEW)

    head = tkinter.Label(frameCima,text="Dados da Empresa", font="arial 18 bold italic", fg='purple')
    head.place(x=110, y=10)


    nmemp = tkinter.Label(frameCima,text="Estabelecimento:",font="arial 12 bold", fg='purple')
    nmemp.place(x=20, y=60)
    nm_emp = tkinter.Entry(frameCima,width=60)
    nm_emp.place(x=20, y=85)

    cnpj = tkinter.Label(frameCima,justify='left',highlightthickness=1,anchor="nw",text="CNPJ", fg="purple", font="arial 12 bold")
    cnpj.place(x=410,y=60)
    cnpj_1 = tkinter.Entry(frameCima,width=24)
    cnpj_1.place(x=410,y=85)

    cnae = tkinter.Label(frameCima,justify='left',highlightthickness=1,anchor="nw",text="CNAE", fg="purple", font="arial 12 bold")
    cnae.place(x=590,y=60)
    cnae_1 = tkinter.Entry(frameCima,width=24)
    cnae_1.place(x=590,y=85)

    edrc = tkinter.Label(frameCima,justify='left',highlightthickness=1,anchor="nw",text="Endereço:",font="arial 12 bold",fg='purple')
    edrc.place(x=20,y=115)
    edrc_cl = tkinter.Entry(frameCima,width=60)
    edrc_cl.place(x=20,y=145)

    cnpj = tkinter.Label(frameCima,justify='left',highlightthickness=1,anchor="nw",text="Cidade", fg="purple", font="arial 12 bold")
    cnpj.place(x=410,y=115)
    cnpj_1 = tkinter.Entry(frameCima,width='18')
    cnpj_1.place(x=410,y=145)

    cnae = tkinter.Label(frameCima,justify='left',highlightthickness=1,anchor="nw",text="UF", fg="purple", font="arial 12 bold")
    cnae.place(x=550,y=115)
    cnae_1 = tkinter.Entry(frameCima,width=5)
    cnae_1.place(x=550,y=145)
    
    cnae = tkinter.Label(frameCima,justify='left',highlightthickness=1,anchor="nw",text="CEP", fg="purple", font="arial 12 bold")
    cnae.place(x=605,y=115)
    cnae_1 = tkinter.Entry(frameCima,width=15)
    cnae_1.place(x=605,y=145)

    edrc = tkinter.Label(frameCima,justify='left',highlightthickness=1,anchor="nw",text="Complemento",font="arial 12 bold",fg='purple')
    edrc.place(x=20,y=175)
    edrc_cl = tkinter.Entry(frameCima,width=60)
    edrc_cl.place(x=20,y=205)

    ctt = tkinter.Label(frameCima,justify='left',highlightthickness=1,anchor="nw",text="Telefone Celular:",font="arial 12 bold",fg='purple')
    ctt.place(x=20,y=235)
    cli_ctt = tkinter.Entry(frameCima,width=26)
    cli_ctt.place(x=20,y=265)

    ctt1 = tkinter.Label(frameCima,justify='left',highlightthickness=1,anchor="nw",text="Telefone Outros:",font="arial 12 bold",fg='purple')
    ctt1.place(x=200,y=235)
    cli_ctt1 = tkinter.Entry(frameCima,width=26)
    cli_ctt1.place(x=200,y=265)

    email = tkinter.Label(frameCima,justify='left',highlightthickness=1,anchor="nw",text="E-mail:",font="arial 12 bold",fg='purple')
    email.place(x=405,y=235)
    cli_email = tkinter.Entry(frameCima,width=50)
    cli_email.place(x=405,y=265)

    rpt = tkinter.Label(frameCima,text="Responsável Técnico",font="arial 12 bold", fg='purple')
    rpt.place(x=20, y=295)
    nm_rpt = tkinter.Entry(frameCima,width=60)
    nm_rpt.place(x=20, y=325)

    rgp = tkinter.Label(frameCima,justify='left',highlightthickness=1,anchor="nw",text="Registro Profissional", fg="purple", font="arial 12 bold")
    rgp.place(x=410,y=295)
    rgp_1 = tkinter.Entry(frameCima,width=24)
    rgp_1.place(x=410,y=325)

    bnc= tkinter.Button(frameBaixo,text="Nova Conta",fg='purple', width=10,font='Times 12 bold')
    bnc.place(x=5,y=0)

    global tree
     
    lista_itens = ["","",""]

    tree = ttk.Treeview(frameBaixo,selectmode="browse",columns=('column1','column2','column3'), show="headings",height=6)

    tree.column("column1",width=430,minwidth=50,stretch=NO)
    tree.heading("#1",text= 'Nome da Conta')

    tree.column("column2",width=355,minwidth=50,stretch=NO)
    tree.heading("#2",text= 'Tipo')

    tree.column("column3",width=150,minwidth=50,stretch=NO)
    tree.heading("#3",text= 'Saldo Inicial')  

    tree.grid(row=1,column=1)
    tree.place(x=0,y=35)
       
    for lista_itens in lista_itens:
     tree.insert('', 'end', values=lista_itens)
    
    edt= tkinter.Button(frameBaixo,text="Editar",fg='purple', width=10,font='Times 12 bold')
    edt.place(x=738,y=185)

    excl= tkinter.Button(frameBaixo,text="Excluir",fg='purple', width=10,font='Times 12 bold')
    excl.place(x=838,y=185)

    Cad = tkinter.Button(rootdemp,justify='center',text="Salvar",fg='purple', width=10,font='Times 12 bold')
    Cad.place(x=375,y=625)


    rootdemp.mainloop()