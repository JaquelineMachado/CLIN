import tkinter
from tkinter.ttk import *
from tkinter import *
import sqlite3
import customtkinter as ctk
from tkinter import Tk, StringVar, ttk
from tkcalendar import Calendar, DateEntry
from formasdepg import fpg
import pygame, sys, random


def cxx():
    pygame.init()
    rootcx = tkinter.Tk()
    rootcx.geometry("990x680")
    rootcx.title("Sistema Clínica")
    rootcx.wm_iconbitmap(r'c:\\Users\\User\\Desktop\\Clinica Python\\icone\\icone sistema.ico')
    
    frameCima = Frame(rootcx,width=960,height=300,relief=FLAT)
    frameCima.grid(row=0,column=0,pady=0,padx=0,sticky=NSEW)

    frameBaixo = Frame(rootcx,width=1043,height=300,pady=20,bg='MediumPurple1',bd= 15,relief=RIDGE)
    frameBaixo.grid(row=2,column=0,pady=0,padx=1,sticky=NSEW)

    head = tkinter.Label(frameCima,text="Contas do Cliente Serviços & Produtos", font="arial 18 bold italic", fg='purple')
    head.place(x=110, y=10)


    id = tkinter.Label(frameCima,text="ID Cliente:",font="arial 10 bold", fg='purple')
    id.place(x=20, y=60)

    C_id = tkinter.Entry(frameCima)
    C_id.place(x=90, y=60)

    entry = DateEntry(frameCima,width=16,height=28,bordewidth=2,fg_color="MediumPurple1",color="MediumPurple3",hover_color="MediumPurple3",dropdown_fg_color="MediumPurple1",dropdown_text_color="Purple")
    entry.place(x=250,y=60)

    
    serv = tkinter.Label(frameCima, text="Serviços :",font="arial 10 bold", fg='purple')
    serv.place(x=20, y=100)

    serviços = ctk.CTkOptionMenu(frameCima,width=255,values=["Serviços...","Carboxiterapia","Criolipóse","Drenagem Linfática","Endermoterapia","Intradermoterapia","Massagem Modeladora","Massagem Relaxante","Limpeza de pele","Microagulhamento","Peeling de Cristal","Peeling de Diamante","Peeling Químico","Skin Acne","Toxina Botulínica","Radiofrequência","Ultracavitação","Ultrassom de Alta Potência"],fg_color="MediumPurple1",button_color="MediumPurple3",button_hover_color="MediumPurple3",dropdown_fg_color="MediumPurple1",dropdown_text_color="Purple")
    serviços.place(x=100,y=100)

    serv_q = tkinter.Label(frameCima, text="Quantidade :",font="arial 10 bold", fg='purple')
    serv_q.place(x=380, y=100)

    serv_q = tkinter.Entry(frameCima,width=5)
    serv_q.place(x=470,y=100)

    vlsl = tkinter.Label(frameCima, text="Valor Serviços:",font="arial 10 bold", fg='purple')
    vlsl.place(x=520, y=100)

    vls_t = tkinter.Entry(frameCima,width=10)
    vls_t.place(x=625,y=100)
    
    pdr = tkinter.Label(frameCima, text="Produtos :",font="arial 10 bold", fg='purple')
    pdr.place(x=20, y=140)
    produtos = ctk.CTkOptionMenu(frameCima,width=255,values=["Produtos...","Creme Clareador","Gel Redutor","Máscara Facial","Máscara Corporal","Protetor Solar","Sérum Facial","Sérum Labial"],fg_color="MediumPurple1",button_color="MediumPurple3",button_hover_color="MediumPurple3",dropdown_fg_color="MediumPurple1",dropdown_text_color="Purple")
    produtos.place(x=100,y=140)

    pdr_q = tkinter.Label(frameCima, text="Quantidade :",font="arial 10 bold", fg='purple')
    pdr_q.place(x=380, y=140)

    pdr_q = tkinter.Entry(frameCima,width=5)
    pdr_q.place(x=470,y=140)
    
    vpdr_q = tkinter.Label(frameCima, text="Valor Produtos :",font="arial 10 bold", fg='purple')
    vpdr_q.place(x=520, y=140)

    vpdr_t = tkinter.Entry(frameCima,width=10)
    vpdr_t.place(x=625,y=140)

    total = tkinter.Label(frameCima,text='    ',width=14,height=2,anchor=CENTER,font="arial 19 bold",bg='MediumPurple1', fg='white')
    total.place(x=700, y=75)
    total_ = tkinter.Label(frameCima,text="    Valor Total de todos os itens   ",font="arial 10 bold",bg='MediumPurple1', fg='white')
    total_.place(x=700, y=70)

    qtd = tkinter.Label(frameCima,text='   ',width=14,height=2,anchor=CENTER,font="arial 19 bold",bg='MediumPurple1', fg='white')
    qtd.place(x=700, y=150)
    qtd_ = tkinter.Label(frameCima,text="    Quantidaded Total de itens     ",font="arial 10 bold",bg='MediumPurple1', fg='white')
    qtd_.place(x=700, y=145)

     
    tabela_head = ['Nome','Serviço','Quant.S.','Valor S.','Produto','Quant. P.','Valor P.','Total']

    lista_itens = []

    global tree

    tree = ttk.Treeview(frameBaixo,selectmode="extended",columns=tabela_head, show="headings")
 
    vsb = ttk.Scrollbar(frameBaixo,orient="vertical",command=tree.yview)

    hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)
 
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameBaixo.grid_rowconfigure(0,weight=12)
    
    
    
    hd=["center","center","center","center","center","center","center","center"]
    h=[210,187,60,70,185,60,70,95]
    n=0

    for col in tabela_head:
      tree.heading(col, text=col.title(), anchor=CENTER)
    # adjust the column's width to the header string
      tree.column(col, width=h[n],anchor=hd[n])
      n+=1
      

 # inserindo os itens dentro da tabela
    for item in lista_itens:
      tree.insert('', 'end', values=item)


    quantidade = []

    for iten in lista_itens:
        quantidade.append(iten[6])

    Total_valor = sum(quantidade)
    Total_itens = len(quantidade)

    total['text'] = 'R$ {:,.2f}'.format(Total_valor)
    qtd['text'] = Total_itens

    ppg = tkinter.Button(rootcx,text="Pagamento",font="arial 14 bold", fg='purple',command=fpg)
    ppg.place(x=750, y=620)

    def FDPG():
     if ppg == ppg:
       fpg()
       
    rootcx.mainloop()


    

    

