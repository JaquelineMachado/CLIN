import tkinter
import sqlite3
from atualcli import atualc,D_cliente,Pq_cli
import window2
import clint


def cli():
    global cli_ID,cli_name,cli_sex,cli_dob,cli_cpf,cli_rg,cli_contact,cli_contactout,cli_email,cli_addr,cli_pro
    global rootc,regfrom,id,name,sex,dob,cpf,rg,c1,c2,email,addr,pro,filemenu,Voltar,SUBMIT,menubar,Pesquisar,DELETE,UPDATE, Atualizar

    rootc = tkinter.Tk()
    rootc.geometry("700x650")
    rootc.title("Sistema Clínica")

    
    regfrom = tkinter.Label(rootc,justify='left',highlightthickness=1,anchor="nw",text="Cadastro Clientes",font="arial 16 bold italic",fg='purple')
    regfrom.place(x=20,y=20)

    id = tkinter.Label(rootc,justify='left',highlightthickness=1,anchor="nw",text="ID Cliente:",font="arial 12 bold",fg='purple')
    id.place(x=20,y=50)
    cli_ID = tkinter.Entry(rootc,width=12,justify='left')
    cli_ID.place(x=50,y=75)

    name = tkinter.Label(rootc,justify='left',highlightthickness=1,anchor="nw",text="Nome Cliente:",font="arial 12 bold",fg='purple')
    name.place(x=20,y=95)
    cli_name = tkinter.Entry(rootc,width=50)
    cli_name.place(x=50,y=120)
    
    sex = tkinter.Label(rootc,justify='left',highlightthickness=1,anchor="nw",text="Sexo:",font="arial 12 bold",fg='purple')
    sex.place(x=20,y=140)
    cli_sex = tkinter.Entry(rootc,width=12)
    cli_sex.place(x=50,y=168)

    dob = tkinter.Label(rootc,justify='left',highlightthickness=1,anchor="nw",text="Data Nascimento: (DD-MM-YYYY)",font="arial 12 bold",fg='purple')
    dob.place(x=20,y=190)
    cli_dob = tkinter.Entry(rootc,width=12)
    cli_dob.place(x=50,y=216)

    cpf = tkinter.Label(rootc,justify='left',highlightthickness=1,anchor="nw",text="CPF:",font="arial 12 bold",fg='purple')
    cpf.place(x=20,y=235)
    cli_cpf = tkinter.Entry(rootc,width=12)
    cli_cpf.place(x=50,y=260)

    rg = tkinter.Label(rootc,justify='left',highlightthickness=1,anchor="nw",text="RG:",font="arial 12 bold",fg='purple')
    rg.place(x=20,y=280)
    cli_rg = tkinter.Entry(rootc,width=12)
    cli_rg.place(x=50,y=305)

    c1 = tkinter.Label(rootc,justify='left',highlightthickness=1,anchor="nw",text="Telefone Celular:",font="arial 12 bold",fg='purple')
    c1.place(x=20,y=325)
    cli_contact = tkinter.Entry(rootc,width=26)
    cli_contact.place(x=50,y=350)

    c2 = tkinter.Label(rootc,justify='left',highlightthickness=1,anchor="nw",text="Telefone Outros:",font="arial 12 bold",fg='purple')
    c2.place(x=20,y=370)
    cli_contactout = tkinter.Entry(rootc,width=26)
    cli_contactout.place(x=50,y=395)

    email = tkinter.Label(rootc,justify='left',highlightthickness=1,anchor="nw",text="E-mail:",font="arial 12 bold",fg='purple')
    email.place(x=20,y=415)
    cli_email = tkinter.Entry(rootc,width=50)
    cli_email.place(x=50,y=440)

    addr = tkinter.Label(rootc,justify='left',highlightthickness=1,anchor="nw",text="Endereço:",font="arial 12 bold",fg='purple')
    addr.place(x=20,y=460)
    cli_addr = tkinter.Entry(rootc,width=50)
    cli_addr.place(x=50,y=485)

    pro = tkinter.Label(rootc,justify='left',highlightthickness=1,anchor="nw",text="Profissional:",font="arial 12 bold",fg='purple')
    pro.place(x=20,y=505)
    cli_pro = tkinter.Entry(rootc,width=30)
    cli_pro.place(x=50,y=530)

    Voltar = tkinter.Button(rootc,text="< Voltar",fg='purple', width=10,font='Times 12 bold',command=window2)
    Pesquisar = tkinter.Button(rootc,text="Pesquisar",fg='purple', width=10,font='Times 12 bold',command=Pq_cli)
    DELETE = tkinter.Button(rootc,text="Deletar",fg='purple', width=10,font='Times 12 bold',command=D_cliente)
    Atualizar = tkinter.Button(rootc,text="Atualizar",fg='purple', width=10,font='Times 12 bold',command=atualc)
    SUBMIT = tkinter.Button(rootc,text="Cadastrar",fg='purple', width=10,font='Times 12 bold')
    

    rootc.wm_iconbitmap(r'c:\\Users\\User\\Desktop\\Clinica Python\\icone\\icone sistema.ico')
    
    Voltar.place(x=70,y=570)
    Pesquisar.place(x=180,y=570)
    DELETE.place(x=290,y=570)
    Atualizar.place(x=400,y=570)
    SUBMIT.place(x=510,y=570)

    rootc.mainloop()

    Voltar = None
    Pesquisar = None
    DELETE = None
    Atualizar = None
 
def ATUAL():
  if Atualizar == Atualizar:
     atualc()

def APAGAR():
  if DELETE == DELETE:
     D_cliente()

def PESQUISA():
  if Pesquisar == Pesquisar:
     Pq_cli()

def cliente():
  if Voltar == Voltar:
     clint.hide()
     window2.un_hide()

