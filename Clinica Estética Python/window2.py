import tkinter
from tkinter import *
from tkinter.ttk import *
import sqlite3
import tkinter.messagebox as tkMassageBox
from empreg import emp_screen
from clint import cli
from caixa import cxx
from agendamento import janela
from prodeserv import prod_serv
from ddemp import dd_emp
#from login import EXIT


def menu():
 global root1,button1,button2,button3,button4,button5,button6,button7

 root1 = tkinter.Tk()
 root1.geometry("200x500")
 root1.title("Sistema Clínica")
 root1.wm_iconbitmap(r'c:\\Users\\User\\Desktop\\Clinica Python\\icone\\icone sistema.ico')
 m=tkinter.Label(root1, text="Menu",font='Times 16 bold italic',fg='purple')
     
 button1 = tkinter.Button(root1,justify='left',highlightthickness=1,anchor="nw", text="Agendamento",command=AGENDA, bg='MediumPurple1', fg='purple',width=15,font='Times 12')
 button2 = tkinter.Button(root1,justify='left',highlightthickness=1,anchor="nw", text="Clientes", command=CLI, bg='MediumPurple1', fg='purple',width=15,font='Times 12')
 button3 = tkinter.Button(root1,justify='left',highlightthickness=1,anchor="nw", text="Caixa",command=CAIXA, bg='MediumPurple1', fg='purple',width=15,font='Times 12')
 button4 = tkinter.Button(root1,justify='left',highlightthickness=1,anchor="nw", text="Profissional",command=PROF, bg='MediumPurple1', fg='purple',width=15,font='Times 12')
 button5 = tkinter.Button(root1,justify='left',highlightthickness=1,anchor="nw",text="Produtos e Serviços",command=PRSR, bg='MediumPurple1', fg='purple',width=15,font='Times 12')
 button6 = tkinter.Button(root1,justify='left',highlightthickness=1,anchor="nw", text="Configurações",command=DDEMP, bg='MediumPurple1', fg='purple',width=15,font='Times 12')
 button7 = tkinter.Button(root1,justify='left',highlightthickness=1,anchor="nw", text="Sair",command=EXIT, bg='MediumPurple1', fg='purple', width=15,font='Times 12')
 
 m.place(x=20,y=-2)

 button1.pack(side=tkinter.TOP)
 button1.place(x=20,y=25)
    
 button2.pack(side=tkinter.TOP)
 button2.place(x=20,y=55)
    
 button3.pack(side=tkinter.TOP)
 button3.place(x=20,y=85)
    
 button4.pack(side=tkinter.TOP)
 button4.place(x=20,y=115)
    
 button5.pack(side=tkinter.TOP)
 button5.place(x=20,y=145)
    
 button6.pack(side=tkinter.TOP)
 button6.place(x=20,y=175)
    
 button7.pack(side=tkinter.TOP)
 button7.place(x=20,y=205)

 root1.mainloop()

 voltar = None
 SEARCH = None
 DELETE = None
 UPDATE = None
 NOVO = None


def EXIT():
 result = tkMassageBox.askquestion('Sistema Clínica','Deseja sair?')
 if result == 'Sim':
   menu.destroy()
   menu.exit()
  
def PROF():
  if button4 == button4:
    emp_screen()

def CLI():
  if button2 == button2:
    cli()

def CAIXA():
  if button3 == button3:
    cxx()

def AGENDA():
  if button1 == button1:
    janela()

def PRSR():
  if button5 == button5:
    prod_serv()
   
def DDEMP():
  if button6 == button6:
    dd_emp()




    




