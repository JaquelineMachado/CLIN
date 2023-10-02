from tkinter import *
from tkinter.ttk import *
from tkinter import PhotoImage
from tkinter import Tk, StringVar, ttk
from PIL import Image, ImageTk
import sqlite3
import tkinter
import customtkinter as ctk
from tkcalendar import Calendar, DateEntry
from datetime import date
import pygame

def janela():
 pygame.init()
 janela = ctk.CTk()

 janela.geometry("1100x600")
 janela.title("Sistema Clínica")
 janela.wm_iconbitmap(r'c:\\Users\\User\\Desktop\\Clinica Python\\icone\\icone sistema.ico')
       
 agenda = tkinter.Label(janela,justify='left',highlightthickness=1,anchor="nw",text="Agenda",font="arial 16 bold italic",fg='purple')
 agenda.place(x=20,y=10)

 tabview = ctk.CTkTabview(janela, width=1070, height=550,fg_color="white",segmented_button_fg_color="MediumPurple1",segmented_button_selected_hover_color="MediumPurple3",segmented_button_unselected_hover_color="MediumPurple1",segmented_button_unselected_color="MediumPurple1")
 tabview.place(x=20,y=40)
 tabview.add("Calendário")
 tabview.add("Venda")
 tabview.add("Profissional")
 tabview.add("Histórico")
 tabview.tab("Venda").grid_columnconfigure(40,weight=40)
 tabview.tab("Profissional").grid_columnconfigure(40,weight=40)
 tabview.tab("Calendário").grid_columnconfigure(40,weight=40)
 tabview.tab("Histórico").grid_columnconfigure(40,weight=40,)

 entry = ctk.CTkEntry(tabview.tab("Calendário"),width=190,placeholder_text="Cliente...")
 entry.place(x=5,y=20)


 '''img= tkinter.PhotoImage(file =r'c:\\Users\\User\\Desktop\\Clinica Python\\icone\\Pessoa.png')
 img=img.subsample(55,60)
 Cad = tkinter.Button(tabview.tab("Calendário"), width=25, image= img)
 labelimg=tkinter.Label(image=img)
 Cad.place(x=196,y=20)'''

 '''image= tkinter.PhotoImage(file =r'c:\\Users\\User\\Desktop\\Clinica Python\\icone\\lupa.png')
 image=image.subsample(60,55)
 pq = tkinter.Button(tabview.tab("Calendário"), width=25, image= image)
 labelimage=tkinter.Label(image=image)
 pq.place(x=229,y=20)'''

 entry = ctk.CTkEntry(tabview.tab("Calendário"),width=124,justify='center',placeholder_text="(  )_____-____")
 entry.place(x=5,y=60)

 entry = ctk.CTkEntry(tabview.tab("Calendário"),width=124,justify='center',placeholder_text="Nascimento")
 entry.place(x=136,y=60)

 entry = ctk.CTkEntry(tabview.tab("Calendário"),width=190,placeholder_text="Serviço...")
 entry.place(x=5,y=100)

 Cadt = tkinter.Button(tabview.tab("Calendário"), width=3,text="+", fg="purple", font="arial 10 bold")
 Cadt.place(x=196,y=100)

 '''magee= tkinter.PhotoImage(file =r'c:\\Users\\User\\Desktop\\Clinica Python\\icone\\lp.png')
 magee=magee.subsample(60,55)
 pps = tkinter.Button(tabview.tab("Calendário"), width=25, image=magee)
 labelmagee=tkinter.Label(image=magee)
 pps.place(x=229,y=100)'''

 entry = DateEntry(tabview.tab("Calendário"),width=16,height=28,bordewidth=2,fg_color="MediumPurple1",color="MediumPurple3",hover_color="MediumPurple3",dropdown_fg_color="MediumPurple1",dropdown_text_color="Purple")
 entry.place(x=5,y=140)

 entry = ctk.CTkEntry(tabview.tab("Calendário"),width=124,justify='left',placeholder_text="  :  ")
 entry.place(x=136,y=140)

 duracao = ctk.CTkOptionMenu(tabview.tab("Calendário"),width=255,values=["Duração...","30 minutos","40 minutos","50 minutos","1 hora","1 hora e 30 minutos","1 hora e 40 minutos","1 hora e 50 minutos","2 horas"],fg_color="MediumPurple1",button_color="MediumPurple3",button_hover_color="MediumPurple3",dropdown_fg_color="MediumPurple1",dropdown_text_color="Purple")
 duracao.place(x=5,y=180)

 prof = ctk.CTkOptionMenu(tabview.tab("Calendário"),width=255,values=["Profissional...","Jaqueline Machado"],fg_color="MediumPurple1",button_color="MediumPurple3",button_hover_color="MediumPurple3",dropdown_fg_color="MediumPurple1",dropdown_text_color="Purple")
 prof.place(x=5,y=220)

 entry = ctk.CTkEntry(tabview.tab("Calendário"),width=255,justify='left',placeholder_text="Observação...")
 entry.place(x=5,y=260)

 stat = ctk.CTkOptionMenu(tabview.tab("Calendário"),width=255,values=["Selecione Status...","Agendado","Atendendo","Atendido","Atrasado","Cancelado","Confirmado","Faltou"],fg_color="MediumPurple1",button_color="MediumPurple3",button_hover_color="MediumPurple3",dropdown_fg_color="MediumPurple1",dropdown_text_color="Purple")
 stat.place(x=5,y=300)

 sms = tkinter.Label(tabview.tab("Calendário"),justify='left',text="Enviar SMS", fg="purple", font="arial 10")
 sms.place(x=110,y=350)

 sim = tkinter.Button(tabview.tab("Calendário"),justify='left',text="SIM", fg="purple", font="arial 10")
 sim.place(x=184,y=350)

 nao = tkinter.Button(tabview.tab("Calendário"), justify='left',text="NÃO", fg="purple", font="arial 10")
 nao.place(x=218,y=350)

 salvar = tkinter.Button(tabview.tab("Calendário"),text="Salvar",fg='purple', width=10,font='Times 12 bold')
 salvar.place(x=5,y=450)
#=========================================================================================================================
    # verificar por que não está funcionando
 
 global tree,trees

 def segmented_button_callback(values):
   text_var.set("")  
   if values == "Dia":
     text_var.set(f"Dia:{tree.get()}")
   if values == "Semana":
     text_var.set(f"Semana:{trees.get()}")
   if values == "Mês":
     text_var.set(f"Mês:{entryM.get()}") 

 segmented = ctk.CTkSegmentedButton(tabview.tab("Calendário"),values=["Dia","Semana","Mês"],fg_color="MediumPurple1",selected_hover_color="MediumPurple3",unselected_hover_color="MediumPurple1",unselected_color="MediumPurple1",command= segmented_button_callback)
 segmented.place(x=900,y=10)
 segmented.set("Dia")

 text_var = tkinter.StringVar(values="")

 label = ctk.CTkLabel(tabview.tab("Calendário"),textvariable = text_var)
 label.place(x=350,y=80)

 #============================================================================================================
   # Mês vai abrir o calendário(verificar tamanho)
 entryM = DateEntry(tabview.tab("Calendário"),width=500,height=500,bordewidth=2,fg_color="MediumPurple1",color="MediumPurple3",hover_color="MediumPurple3",dropdown_fg_color="MediumPurple1",dropdown_text_color="Purple")
 entryM.place(x=5,y=140)

 #==============================================================================================================
   # Dia

 global tree,trees
 
 tabela_head = ['Hora','Nome']

 lista_itens = ['8',' ', '8:30',' ','9:00',' ','9:30',' ','10:00',' ','10:30',' ','11:00',' ','11:30',' ','12:00',' ','12:30',' ','13:00',' ','13:30',' ','14:00',' ','14:30',' ','15:00',' ','16:00',' ','16:30',' ','17:00',' ','17:30',' ','18:00',' ','18:30']

 tree = ttk.Treeview(tabview.tab("Calendário"),selectmode="extended",columns=tabela_head, show="headings",height=18)
 
 vsb = ttk.Scrollbar(tabview.tab("Calendário"),orient="vertical",command=tree.yview)
 # vertical scrollbar
 tree.configure(yscrollcommand=vsb.set)
 tree.grid(column=0, row=0, sticky='nsew')
 vsb.grid(column=2, row=0, sticky='ns')
 vsb.place(x=1023,y=105)

    
 hd=["center","center"]
 h=[40,650]
 n=0

 for col in tabela_head:
    tree.heading(col, text=col.title(), anchor=CENTER)
    # adjust the column's width to the header string
    tree.column(col, width=h[n],anchor=hd[n])
    n+=1
    tree.place(x=350,y=80)

 # inserindo os itens dentro da tabela
 for item in lista_itens:
    tree.insert('', 'end', values=item)

#===========================================================================================
   # Semanal

 tabela_head = ['Hora','Segunda','Terça','Quarta','Quinta','Sexta','Sábado']

 lista_itens = ['8',' ', '8:30',' ','9:00',' ','9:30',' ','10:00',' ','10:30',' ','11:00',' ','11:30',' ','12:00',' ','12:30',' ','13:00',' ','13:30',' ','14:00',' ','14:30',' ','15:00',' ','16:00',' ','16:30',' ','17:00',' ','17:30',' ','18:00',' ','18:30']

 trees = ttk.Treesview(tabview.tab("Calendário"),selectmode="extended",columns=tabela_head, show="headings",height=18)
 
 vsb = ttk.Scrollbar(tabview.tab("Calendário"),orient="vertical",command=trees.yview)
 # vertical scrollbar
 trees.configure(yscrollcommand=vsb.set)
 trees.grid(column=0, row=0, sticky='nsew')
 vsb.grid(column=2, row=0, sticky='ns')
 vsb.place(x=1023,y=105)

    
 hd=["center","center","center","center","center","center","center"]
 h=[40,100,100,100,100,100,100]
 n=0

 for col in tabela_head:
    trees.heading(col, text=col.title(), anchor=CENTER)
    # adjust the column's width to the header string
    trees.column(col, width=h[n],anchor=hd[n])
    n+=1
    trees.place(x=350,y=80)

 # inserindo os itens dentro da tabela
 for item in lista_itens:
    trees.insert('', 'end', values=item)

# ==========================================================================================
    # vendas

 frame1 = Frame(tabview.tab("Venda"),relief=RIDGE)
 frame1.grid()

 '''framelde = Frame(frameLdd1,width=500,height=200,bg='MediumPurple1',bd= 10,relief=RIDGE)
    framelde.grid(row=1,column=5,sticky=E)'''


 frame1 = ctk.CTkFrame(tabview.tab("Venda"), width=330, height=300,fg_color='white',bg_color='MediumPurple1',border_width=3)
 frame1.grid(row=3,column=1,pady=0,padx=2)

 head = tkinter.Label(frame1,text="Cliente", font="arial 14 bold italic", fg='purple')
 head.place(x=10, y=10)
 
 entry = ctk.CTkEntry(frame1,width=190,placeholder_text="Cliente...")
 entry.place(x=5,y=50)

 entry1 = ctk.CTkEntry(frame1,width=100,placeholder_text="( )_____-____")
 entry1.place(x=5,y=90)

 pqsc = tkinter.Button(frame1, justify='left',text="Pesquisar", fg="purple", font="arial 10")
 pqsc.place(x=110,y=90)
#=============================================================================================
    #vendas

 frame2 = Frame(tabview.tab("Venda"),relief=RIDGE)
 frame2.grid()

 frame2 = ctk.CTkFrame(tabview.tab("Venda"),width=330,height=300,fg_color='white',bg_color='MediumPurple1',border_width= 3)
 frame2.grid(row=3,column=2,pady=0,padx=2)

 head2 = tkinter.Label(frame2,text="Produtos/Serviços", font="arial 14 bold italic", fg='purple')
 head2.place(x=10, y=10)

 entry2 = ctk.CTkEntry(frame2,width=205,placeholder_text="Informe Produto/Serviço")
 entry2.place(x=5,y=50)

 prof = ctk.CTkOptionMenu(frame2,width=205,values=["Profissional...","Jaqueline Machado"],fg_color="MediumPurple1",button_color="MediumPurple3",button_hover_color="MediumPurple3",dropdown_fg_color="MediumPurple1",dropdown_text_color="Purple")
 prof.place(x=5,y=90)

 entry3 = ctk.CTkEntry(frame2,width=100,placeholder_text="Preço...")
 entry3.place(x=5,y=130)

 entry4 = ctk.CTkEntry(frame2,width=100,placeholder_text="Quant...")
 entry4.place(x=110,y=130)
 
 btv = tkinter.Button(frame2, justify='left',text="+ Incluir na Venda", fg="purple", font="arial 10")
 btv.place(x=190,y=180)


#====================================================================================================
  # vendas

 frame3 = Frame(tabview.tab("Venda"),relief=RIDGE)
 frame3.grid()


 frame3 = ctk.CTkFrame(tabview.tab("Venda"),width=330,height=300,fg_color='white',bg_color='MediumPurple1',border_width= 3)
 frame3.grid(row=3,column=3,pady=0,padx=2,sticky=E)

 head3 = tkinter.Label(frame3,text="Informações da Venda", font="arial 14 bold italic", fg='purple')
 head3.place(x=10, y=10)
 
 dtcl= tkinter.Label(frame3,justify='left',highlightthickness=1,anchor="nw",text="Data",font="arial 11 bold italic",fg='purple')
 dtcl.place(x=5,y=50)

 entry5 = DateEntry(frame3,width=16,height=28,bordewidth=2,fg_color="MediumPurple1",color="MediumPurple3",hover_color="MediumPurple3",dropdown_fg_color="MediumPurple1",dropdown_text_color="Purple")
 entry5.place(x=5,y=85)

 ttlcl= tkinter.Label(frame3,justify='left',highlightthickness=1,anchor="nw",text="Total",font="arial 11 bold italic",fg='purple')
 ttlcl.place(x=120,y=50)
 
 entry6 = ctk.CTkEntry(frame3,width=100,placeholder_text="Total")
 entry6.place(x=130,y=85)

 button1 = tkinter.Button(frame3, text="$ Formas de Pagamento",justify='center', bg='MediumPurple1', fg='purple',width=35,font='Times 12')
 button1.place(x=3,y=150)  

#===================================================================================================
 
 
 
 clt_prf= tkinter.Label(tabview.tab("Profissional"),justify='left',highlightthickness=1,anchor="nw",text="Cliente",font="arial 12 bold italic",fg='purple')
 clt_prf.place(x=20,y=10)
 
 entry7 = ctk.CTkEntry(tabview.tab("Profissional"),width=170,placeholder_text="Cliente...")
 entry7.place(x=20,y=50)

 servcl= tkinter.Label(tabview.tab("Profissional"),justify='left',highlightthickness=1,anchor="nw",text="Serviço",font="arial 12 bold italic",fg='purple')
 servcl.place(x=210,y=10)
 
 entry8 = ctk.CTkEntry(tabview.tab("Profissional"),width=170,placeholder_text="Serviço...")
 entry8.place(x=210,y=50)

 pqdt= tkinter.Label(tabview.tab("Profissional"),justify='left',highlightthickness=1,anchor="nw",text="Intervalo do Período",font="arial 12 bold italic",fg='purple')
 pqdt.place(x=400,y=10)

 entry9 = DateEntry(tabview.tab("Profissional"),width=16,height=28,bordewidth=2,fg_color="MediumPurple1",color="MediumPurple3",hover_color="MediumPurple3",dropdown_fg_color="MediumPurple1",dropdown_text_color="Purple")
 entry9.place(x=400,y=50)
 
 pqdt= tkinter.Label(tabview.tab("Profissional"),justify='left',highlightthickness=1,anchor="nw",text="até",font="arial 12 bold italic",fg='purple')
 pqdt.place(x=520,y=50)

 entry10 = DateEntry(tabview.tab("Profissional"),width=16,height=28,bordewidth=2,fg_color="MediumPurple1",color="MediumPurple3",hover_color="MediumPurple3",dropdown_fg_color="MediumPurple1",dropdown_text_color="Purple")
 entry10.place(x=550,y=50)
 
 pqprof= tkinter.Label(tabview.tab("Profissional"),justify='left',highlightthickness=1,anchor="nw",text="Profissionais",font="arial 12 bold italic",fg='purple')
 pqprof.place(x=690,y=10)


 profpf = ctk.CTkOptionMenu(tabview.tab("Profissional"),width=255,values=["Profissional...","Jaqueline Machado"],fg_color="MediumPurple1",button_color="MediumPurple3",button_hover_color="MediumPurple3",dropdown_fg_color="MediumPurple1",dropdown_text_color="Purple")
 profpf.place(x=690,y=50)

 button2 = tkinter.Button(tabview.tab("Profissional"), text="Pesquisar", justify="center", fg='purple',width=15,font='Times 12')
 button2.place(x=850,y=120)

 global tree1
     
 lista_itens = ["","","","","",""]

 tree1 = ttk.Treeview(tabview.tab("Profissional"),selectmode="browse",columns=('column1','column2','column3','column4'), show="headings",height=6)

 tree1.column("column1",width=330,minwidth=50,stretch=NO)
 tree1.heading("#1",text= 'Cliente')

 tree1.column("column2",width=300,minwidth=50,stretch=NO)
 tree1.heading("#2",text= 'Serviço')

 tree1.column("column3",width=180,minwidth=50,stretch=NO)
 tree1.heading("#3",text= 'Data do Atendimento')  

 tree1.column("column4",width=180,minwidth=50,stretch=NO)
 tree1.heading("#4",text= 'Profissionais')

 tree1.grid(row=1,column=1)
 tree1.place(x=0,y=200)
       
 for lista_itens in lista_itens:
   tree1.insert('', 'end', values=lista_itens)
#================================================================================

 clt_prf= tkinter.Label(tabview.tab("Histórico"),justify='left',highlightthickness=1,anchor="nw",text="Cliente",font="arial 12 bold italic",fg='purple')
 clt_prf.place(x=20,y=10)
 
 entry7 = ctk.CTkEntry(tabview.tab("Histórico"),width=170,placeholder_text="Cliente...")
 entry7.place(x=20,y=50)

 servcl= tkinter.Label(tabview.tab("Histórico"),justify='left',highlightthickness=1,anchor="nw",text="Serviço",font="arial 12 bold italic",fg='purple')
 servcl.place(x=210,y=10)
 
 entry8 = ctk.CTkEntry(tabview.tab("Histórico"),width=170,placeholder_text="Serviço...")
 entry8.place(x=210,y=50)

 pqdt= tkinter.Label(tabview.tab("Histórico"),justify='left',highlightthickness=1,anchor="nw",text="Intervalo do Período",font="arial 12 bold italic",fg='purple')
 pqdt.place(x=400,y=10)

 entry9 = DateEntry(tabview.tab("Histórico"),width=16,height=28,bordewidth=2,fg_color="MediumPurple1",color="MediumPurple3",hover_color="MediumPurple3",dropdown_fg_color="MediumPurple1",dropdown_text_color="Purple")
 entry9.place(x=400,y=50)
 
 pqdt= tkinter.Label(tabview.tab("Histórico"),justify='left',highlightthickness=1,anchor="nw",text="até",font="arial 12 bold italic",fg='purple')
 pqdt.place(x=520,y=50)

 entry10 = DateEntry(tabview.tab("Histórico"),width=16,height=28,bordewidth=2,fg_color="MediumPurple1",color="MediumPurple3",hover_color="MediumPurple3",dropdown_fg_color="MediumPurple1",dropdown_text_color="Purple")
 entry10.place(x=550,y=50)
 
 pqprof= tkinter.Label(tabview.tab("Histórico"),justify='left',highlightthickness=1,anchor="nw",text="Profissionais",font="arial 12 bold italic",fg='purple')
 pqprof.place(x=690,y=10)


 profpf = ctk.CTkOptionMenu(tabview.tab("Histórico"),width=255,values=["Profissional...","Jaqueline Machado"],fg_color="MediumPurple1",button_color="MediumPurple3",button_hover_color="MediumPurple3",dropdown_fg_color="MediumPurple1",dropdown_text_color="Purple")
 profpf.place(x=690,y=50)

 button2 = tkinter.Button(tabview.tab("Histórico"), text="Pesquisar", justify="center", fg='purple',width=15,font='Times 12')
 button2.place(x=850,y=120)

 global tree2
     
 lista_itens = ["","","","","",""]

 tree2 = ttk.Treeview(tabview.tab("Histórico"),selectmode="browse",columns=('column1','column2','column3','column4'), show="headings",height=6)

 tree2.column("column1",width=330,minwidth=50,stretch=NO)
 tree2.heading("#1",text= 'Cliente')

 tree2.column("column2",width=300,minwidth=50,stretch=NO)
 tree2.heading("#2",text= 'Serviço')

 tree2.column("column3",width=180,minwidth=50,stretch=NO)
 tree2.heading("#3",text= 'Data do Atendimento')  

 tree2.column("column4",width=180,minwidth=50,stretch=NO)
 tree2.heading("#4",text= 'Profissionais')

 tree2.grid(row=1,column=1)
 tree2.place(x=0,y=200)
       
 for lista_itens in lista_itens:
   tree2.insert('', 'end', values=lista_itens)

 
 janela.mainloop()


