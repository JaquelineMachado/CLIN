import tkinter
import sqlite3
import tkinter.messagebox


def Pq_cli():
 rootpq = tkinter.Tk()
 rootpq.geometry("400x200")
 rootpq.title("Sistema Clínica")
 rootpq.wm_iconbitmap(r'c:\\Users\\User\\Desktop\\Clinica Python\\icone\\icone sistema.ico')

 pq = tkinter.Label(rootpq,text="Digite o ID do Cliente para PESQUISAR",font="arial 12 bold italic",fg='purple')
 pq.place(x=50,y=40)

 entry1 = tkinter.Entry(rootpq)
 entry1.place(x=140,y=80)

 Pqc= tkinter.Button(rootpq,text="Pesquisar",fg='purple', width=10,font='Times 12 bold')
 Pqc.place(x=150,y=105)

 
 rootpq.mainloop()


def D_cliente():
 rootD = tkinter.Tk()
 rootD.geometry("400x200")
 rootD.title("Sistema Clínica")
 rootD.wm_iconbitmap(r'c:\\Users\\User\\Desktop\\Clinica Python\\icone\\icone sistema.ico')

 d = tkinter.Label(rootD,text="Digite o ID do Cliente para DELETAR",font="arial 12 bold italic",fg='purple')
 d.place(x=50,y=40)

 entry1 = tkinter.Entry(rootD)
 entry1.place(x=140,y=80)

 DeleteD = tkinter.Button(rootD,text="Deletar",fg='purple', width=10,font='Times 12 bold')
 DeleteD.place(x=150,y=105)

 
 rootD.mainloop()


def atualc():
 global cli_ID,cli_name,cli_sex,cli_dob,cli_cpf,cli_rg,cli_contact,cli_contactout,cli_email,cli_addr,cli_pro
 global roota,a,id,name,sex,dob,cpf,rg,c1,c2,email,addr,pro,filemenu,back,SUBMIT,menubar,SEARCH,DELETE,UPDATE


 roota = tkinter.Tk()
 roota.geometry("600x680")
 roota.title("Sistema Clínica")
 roota.wm_iconbitmap(r'c:\\Users\\User\\Desktop\\Clinica Python\\icone\\icone sistema.ico')

 
 a = tkinter.Label(roota,justify='left',highlightthickness=1,anchor="nw",text="Atualizar Clientes",font="arial 16 bold italic",fg='purple')
 a.place(x=20,y=20)

 id = tkinter.Label(roota,justify='left',highlightthickness=1,anchor="nw",text="ID Cliente:",font="arial 12 bold",fg='purple')
 id.place(x=20,y=50)
 cli_ID = tkinter.Entry(roota,width=12,justify='left')
 cli_ID.place(x=50,y=75)

 name = tkinter.Label(roota,justify='left',highlightthickness=1,anchor="nw",text="Nome Cliente:",font="arial 12 bold",fg='purple')
 name.place(x=20,y=95)
 cli_name = tkinter.Entry(roota,width=50)
 cli_name.place(x=50,y=120)
    
 sex = tkinter.Label(roota,justify='left',highlightthickness=1,anchor="nw",text="Sexo:",font="arial 12 bold",fg='purple')
 sex.place(x=20,y=140)
 cli_sex = tkinter.Entry(roota,width=12)
 cli_sex.place(x=50,y=168)

 dob = tkinter.Label(roota,justify='left',highlightthickness=1,anchor="nw",text="Data Nascimento: (DD-MM-YYYY)",font="arial 12 bold",fg='purple')
 dob.place(x=20,y=190)
 cli_dob = tkinter.Entry(roota,width=12)
 cli_dob.place(x=50,y=216)

 cpf = tkinter.Label(roota,justify='left',highlightthickness=1,anchor="nw",text="CPF:",font="arial 12 bold",fg='purple')
 cpf.place(x=20,y=235)
 cli_cpf = tkinter.Entry(roota,width=12)
 cli_cpf.place(x=50,y=260)

 rg = tkinter.Label(roota,justify='left',highlightthickness=1,anchor="nw",text="RG:",font="arial 12 bold",fg='purple')
 rg.place(x=20,y=280)
 cli_rg = tkinter.Entry(roota,width=12)
 cli_rg.place(x=50,y=305)

 c1 = tkinter.Label(roota,justify='left',highlightthickness=1,anchor="nw",text="Telefone Celular:",font="arial 12 bold",fg='purple')
 c1.place(x=20,y=325)
 cli_contact = tkinter.Entry(roota,width=26)
 cli_contact.place(x=50,y=350)

 c2 = tkinter.Label(roota,justify='left',highlightthickness=1,anchor="nw",text="Telefone Outros:",font="arial 12 bold",fg='purple')
 c2.place(x=20,y=370)
 cli_contactout = tkinter.Entry(roota,width=26)
 cli_contactout.place(x=50,y=395)

 email = tkinter.Label(roota,justify='left',highlightthickness=1,anchor="nw",text="E-mail:",font="arial 12 bold",fg='purple')
 email.place(x=20,y=415)
 cli_email = tkinter.Entry(roota,width=50)
 cli_email.place(x=50,y=440)

 addr = tkinter.Label(roota,justify='left',highlightthickness=1,anchor="nw",text="Endereço:",font="arial 12 bold",fg='purple')
 addr.place(x=20,y=460)
 cli_addr = tkinter.Entry(roota,width=50)
 cli_addr.place(x=50,y=485)

 pro = tkinter.Label(roota,justify='left',highlightthickness=1,anchor="nw",text="Profissional:",font="arial 12 bold",fg='purple')
 pro.place(x=20,y=505)
 cli_pro = tkinter.Entry(roota,width=30)
 cli_pro.place(x=50,y=530)

 
 Atualizar = tkinter.Button(roota,text="Atualizar",fg='purple', width=10,font='Times 12 bold')

    
 
 Atualizar.place(x=250,y=570)
 
    
 roota.mainloop()
