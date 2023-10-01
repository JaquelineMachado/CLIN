from tkinter import *
import sqlite3
import tkinter
import customtkinter as ctk
from tkinter import Tk, StringVar, ttk
from tkcalendar import Calendar, DateEntry
import time
import datetime
import pygame, sys, random
import tkinter.messagebox as tkMassageBox

def fpg():
    pygame.init()
    rootfpg = Tk()
    rootfpg.geometry("900x600")
    rootfpg.title("Sistema Clínica")
    rootfpg.wm_iconbitmap(r'c:\\Users\\User\\Desktop\\Clinica Python\\icone\\icone sistema.ico')
        
    frameLdd = Frame(rootfpg,relief=FLAT)
    frameLdd.grid()

    frameLdd1 = Frame(frameLdd,width=600,height=300,relief=FLAT,pady=1)
    frameLdd1.grid(row=0,column=0,sticky=W,columnspan=2)

    txtTitle = Label(frameLdd1,text="Formas de Pagamento", font="arial 18 bold italic", fg='purple')
    txtTitle.grid(row=0,column=0)
    
    Receipt_Ref = StringVar() 
    Tax = StringVar()
    Total = StringVar()
    
    Date1 = StringVar()
    Date1.set(time.strftime("%d\%m\%Y"))
    Date1 = Label(frameLdd1,text="Data da Baixa",justify='left',padx=1,font="arial 10 bold", fg='purple')
    Date1.grid(row=1,column=0,sticky=W,columnspan=1)
    Date1= Entry(frameLdd1,justify='left')
    Date1.grid(row=1,column=1,sticky=W, pady=4)
    
     
    fdp = Label(frameLdd1, text="Formas de Pagamento",justify='left',padx=1,font="arial 10 bold", fg='purple')
    fdp.grid(row=2,column=0,sticky=W)
    fdep = ctk.CTkOptionMenu(frameLdd1,width=255,values=["Formas de Pagamento...","Cartão de Crédito","Cartão de Débito","Dinheiro","PIX"],fg_color="MediumPurple1",button_color="MediumPurple3",button_hover_color="MediumPurple3",dropdown_fg_color="MediumPurple1",dropdown_text_color="Purple")
    fdep.grid(row=2,column=1)
    

    pcl = Label(frameLdd1, text="Parcelas",justify='left',padx=1,font="arial 10 bold", fg='purple')
    pcl.grid(row=3,column=0,sticky=W)
    pcls = ctk.CTkOptionMenu(frameLdd1,width=255,values=["Parcelas...","À Vista","2 parcelas","3 parcelas","4 parcelas","5 parcelas","6 parcelas"],fg_color="MediumPurple1",button_color="MediumPurple3",button_hover_color="MediumPurple3",dropdown_fg_color="MediumPurple1",dropdown_text_color="Purple")
    pcls.grid(row=3,column=1)
    


    framelde = Frame(frameLdd1,width=500,height=200,bg='MediumPurple1',bd= 10,relief=RIDGE)
    framelde.grid(row=1,column=5,sticky=E)

    framelde1 = Frame(framelde,bg='white',relief=RIDGE)
    framelde1.grid(row=0,column=0,sticky=E)

    txtReceipt  = Text(framelde1,height=27,width=30,bd=24,font="arial 9 bold")
    txtReceipt.grid(row=0,column=0)

    framelde2 = Frame(frameLdd1,width=500,height=200,bg='MediumPurple1',bd= 10,relief=RIDGE)
    framelde2.grid(row=2,column=5,columnspan=2,sticky=E)

    btnImpr = Button(framelde2,padx=1,pady=1,bd=4,font="arial 8 bold", fg='purple',width=16,text="Imprimir")
    btnImpr.grid(row=0,column=0)

    btnSr = Button(framelde2,padx=1,pady=1,bd=4,font="arial 8 bold", fg='purple',width=17,text="Sair",command=Exit)
    btnSr.grid(row=0,column=2)
   

    rootfpg.mainloop()

      
    

def Exit():
   result=tkMassageBox.askquestion("Deseja realmente sair?")
   if result == 'Sim':
      fpg.destroy()
      return

    



    