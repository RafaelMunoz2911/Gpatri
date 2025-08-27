from tkinter .ttk import *
from tkinter import Tk, ttk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

#tkcalendar
from datetime import date

from datetime import datetime

hoje = date.today()

#importando as func da view
from crud import *

#CORES

co0 = "#2e2d2b" # essa labels e menu
co1 = "#feffff" # essa labels
co2 = "#4fa882"
co3 = "#38576b" # essa divisorias
co4 = "#403d3d"
co5 = "#e06636"
co6 = "#E9A178"
co7 = "#3fbfb9"
co8 = "#CCB583"  #dourado ourominas
co9 = "#162A0A"  #verde ourominas
co10 = "#5c6369" # essa cor de fundo
co11  = "#f2f4f2"



# criando janela
janela = Tk()
janela.title("")
janela.geometry ('960x350')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

# frames 
frameCima = Frame(janela, width=960, height=50, bg=co8, relief="flat")
frameCima.place(x=0, y=0)

frameEsquerda = Frame(janela, width=150, height=265, bg=co9, relief="solid")
frameEsquerda.place(x=0, y=50)

frameDireita = Frame(janela, width=720, height=300, bg=co1, relief="raised")
frameDireita.place(x=240, y=50)

#novo usuario
def novo_usuario():

    global img_salvar

    def add():
        first_name = e_nome.get()
        setor = e_setor.get()
        email = e_email.get()
        

        lista = [first_name, setor, email]
        
        #verificando caso algum campo esteja vazio
        for i in lista:
            if i=='':
                messagebox.showerror('Erro!!!', 'Preencha todos os campos!!!')
                return
        
        #inserindo os dados no banco de dados
        insert_user(first_name, setor, email)

        messagebox.showinfo('Sucesso!!!', 'Usuario inserido com sucesso!!!')

        #limpando os campos de entrada
        e_nome.delete(0,END)
        e_setor.delete(0,END)
        e_email.delete(0,END)
       

    app_ = Label(frameDireita, text="Adicionar um novo usuário", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=co1, fg=co4)
    app_.place(x=90, y=0)
    app = Label(frameDireita, width=950, height=1, anchor=NW, font=('Verdana 1'), bg=co4, fg=co1)
    app.place(x=0, y=40)

    l_nome = Label(frameDireita, text="Primeiro nome*", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_nome.place(x=200, y=60)
    e_nome = Entry(frameDireita, width=25, justify='left', relief='solid')
    e_nome.place(x=350, y=60)

    l_setor = Label(frameDireita, text="Setor*", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_setor.place(x=200, y=100)
    e_setor = Entry(frameDireita, width=25, justify='left', relief='solid')
    e_setor.place(x=350, y=100)


    l_email = Label(frameDireita, text="E-mail*", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_email.place(x=200, y=140)
    e_email = Entry(frameDireita, width=25, justify='left', relief='solid')
    e_email.place(x=350, y=140)


    #Botão salvar
    img_salvar = Image.open('save.png')
    img_salvar = img_salvar.resize((18,18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDireita,command=add, image=img_salvar, compound=LEFT, width=100, anchor=NW, text=" Salvar", bg=co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.place(x=290, y=180)

#ver usuarios
def ver_usuarios():

    app_ = Label(frameDireita, text="Todos os usuários cadastrados", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    app = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co4, fg=co1)
    app.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    dados = get_users()

    #criando a treevew com duas scrollsbars
    list_header = ['ID', 'Nome', 'Setor', 'Email']
    
    global tree

    tree = ttk.Treeview(frameDireita, selectmode="extended",
                        columns=list_header, show="headings")
    
    #scrollbar vertical
    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)

    #scrollbar horizontal
    hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireita.grid_columnconfigure(0, weight=12)
    
    hd=["nw","nw","nw","nw"]
    h=[50,120,120,120]
    n=0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        #ajustando a largura da coluna ao cabeçalho
        tree.column(col, width=h[n], anchor=hd[n])

        n+=1

    for item in dados:
        tree.insert('', 'end', values=item)

#novo computador
def novo_computador():

    def add():
        ip= e_ip.get()
        patrimonio = e_patrimonio.get()
        hostname = e_hostname.get()
        modelo = e_modelo.get()
        processador = e_processador.get()
        memoria = e_memoria.get()
        armazenamento = e_armazenamento.get()
        monitores = e_q_monitoes.get()
        observacoes= e_observacoes.get()

        lista = [ip, patrimonio, hostname, modelo, processador, memoria, armazenamento, monitores, observacoes]
        
        #verificando caso algum campo esteja vazio
        for i in lista:
            if i=='':
                messagebox.showerror('Erro!!!', 'Preencha todos os campos!!!')
                return
        
        #inserindo os dados no banco de dados
        insert_pc(ip, patrimonio, hostname, modelo, processador, memoria, armazenamento, monitores, observacoes)

        messagebox.showinfo('Sucesso!!!', 'Computador adicionado com sucesso!!!')

        #limpando os campos de entrada
        e_ip.delete(0,END)
        e_patrimonio.delete(0,END)
        e_hostname.delete(0,END)
        e_modelo.delete(0,END)
        e_processador.delete(0,END)
        e_memoria.delete(0,END)
        e_armazenamento.delete(0,END)
        e_q_monitoes.delete(0,END)
        e_observacoes.delete(0,END)
    
    global img_salvar

    app_ = Label(frameDireita, text="Adicionar um novo computador", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=co1, fg=co4)
    app_.place(x=90, y=0)
    app = Label(frameDireita, width=950, height=1, anchor=NW, font=('Verdana 1'), bg=co4, fg=co1)
    app.place(x=0, y=40)

    l_ip = Label(frameDireita, text="Ip*", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_ip.place(x=2, y=60)
    e_ip = Entry(frameDireita, width=20, justify='left', relief='solid')
    e_ip.place(x=115, y=60)

    l_patrimonio = Label(frameDireita, text="Patrimonio*", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_patrimonio.place(x=275, y=60)
    e_patrimonio = Entry(frameDireita, width=20, justify='left', relief='solid')
    e_patrimonio.place(x=370, y=60)

    l_hostname = Label(frameDireita, text="Hostname*", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_hostname.place(x=2, y=100)
    e_hostname = Entry(frameDireita, width=20, justify='left', relief='solid')
    e_hostname.place(x=115, y=100)

    l_modelo = Label(frameDireita, text="Modelo*", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_modelo.place(x=275, y=100)
    e_modelo = Entry(frameDireita, width=20, justify='left', relief='solid')
    e_modelo.place(x=370, y=100)

    l_processador = Label(frameDireita, text="Processador*", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_processador.place(x=2, y=140)
    e_processador = Entry(frameDireita, width=20, justify='left', relief='solid')
    e_processador.place(x=115, y=140)

    l_memoria = Label(frameDireita, text="Memória*", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_memoria.place(x=275, y=140)
    e_memoria = Entry(frameDireita, width=20, justify='left', relief='solid')
    e_memoria.place(x=370, y=140)

    l_armazenamento = Label(frameDireita, text="Armazenamento*", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_armazenamento.place(x=2, y=180)
    e_armazenamento = Entry(frameDireita, width=20, justify='left', relief='solid')
    e_armazenamento.place(x=115, y=180)

    l_q_monitoes = Label(frameDireita, text="Nº Monitoes*", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_q_monitoes.place(x=275, y=180)
    e_q_monitoes = Entry(frameDireita, width=20, justify='left', relief='solid')
    e_q_monitoes.place(x=370, y=180)

    l_observacoes = Label(frameDireita, text="Observações*", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_observacoes.place(x=2, y=220)
    e_observacoes = Entry(frameDireita, width=20, justify='left', relief='solid')
    e_observacoes.place(x=115, y=220) 

    #Botão salvar
    img_salvar = Image.open('save.png')
    img_salvar = img_salvar.resize((18,18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDireita, command=add, image=img_salvar, compound=LEFT, width=100, anchor=NW, text=" Salvar", bg=co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.place(x=275, y=220)

#ver computadores
def ver_computadores():

    app_ = Label(frameDireita, text="Todos os Computadores", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    app = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co4, fg=co1)
    app.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    dados = get_pcs()

    #criando a treevew com duas scrollsbars
    list_header = ['ID', 'IP', 'Património', 'Hostname', 'Modelo', 'Processador', 'Memória', 'Armazenamento', 'Monitores', 'Observações']
    
    global tree

    tree = ttk.Treeview(frameDireita, selectmode="extended", columns=list_header, show="headings")
    
    #scrollbar vertical
    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)

    #scrollbar horizontal
    hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireita.grid_columnconfigure(0, weight=12)
    
    hd=["nw","nw","nw","nw","nw","nw","nw","nw","nw","nw"]
    h=[30,70,70,70,80,80,70,50,30,150]
    n=0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        #ajustando a largura da coluna ao cabeçalho
        tree.column(col, width=h[n], anchor=hd[n])

        n+=1

    for item in dados:
        tree.insert('', 'end', values=item)

#atribuir computadores
def nova_atribuicao():
    
    global img_salvar

    def add():
        id_usuario = e_id_usuario.get()
        id_computador = e_id_computador.get()

        lista = [id_usuario,id_computador]
        
        #verificando caso algum campo esteja vazio
        for i in lista:
            if i=='':
                messagebox.showerror('Erro!!!', 'Preencha todos os campos!!!')
                return
        
        #inserindo os dados no banco de dados
        insert_assignment(id_usuario,id_computador, hoje, None)

        messagebox.showinfo('Sucesso!!!', 'Computador atribuído com sucesso!!!')

        #limpando os campos de entrada
        e_id_computador.delete(0,END)
        e_id_usuario.delete(0,END)

    app_ = Label(frameDireita, text="Realizar uma nova atribuição", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=5, sticky=NSEW)
    app = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
    app.grid(row=1, column=0, columnspan=5, sticky=NSEW)

    l_id_usuario = Label(frameDireita, text="Digite o ID do usuario*", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_id_usuario.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    e_id_usuario = Entry(frameDireita, width=25, justify='left', relief='solid')
    e_id_usuario.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    l_id_computador = Label(frameDireita, text="Digite o ID do computador*", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_id_computador.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    e_id_computador = Entry(frameDireita, width=25, justify='left', relief='solid')
    e_id_computador.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    #Botão salvar
    img_salvar = Image.open('save.png')
    img_salvar = img_salvar.resize((18,18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDireita,command=add, image=img_salvar, compound=LEFT, width=100, anchor=NW, text=" Salvar", bg=co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=7, column=1, padx=5, pady=5, sticky=NSEW)

#criando divisorias "util de mais pra todo projeto"
app = Label(frameCima, width=950, height=1, padx=5, anchor=NW, font=('Verdana 1'), bg=co4, fg=co1)
app.place(x=0, y=47)

# logo 
#abrindo imagens """""importante"""""
app_img = Image.open('logo.png')
app_img = app_img.resize((40,40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, width=1000, compound=LEFT, padx=5, anchor=NW, bg=co8, fg=co1)
app_logo.place(x=5, y=0)

app = Label(frameCima, text="Sistema de Gerenciamento de Patrimónios", compound=LEFT, padx=5, anchor=NW, font=('Verdana 15 bold'), bg=co8, fg=co9)
app.place(x=50, y=7)

#função para controlar o meni
def control(i):
    #novo usuario
    if i == 'novo_usuario':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        #chamando func novo usuario   
        novo_usuario()

    #ver usuaros
    if i == 'ver_usuarios':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        #chamando func novo usuario   
        ver_usuarios()

    #novo_pc
    if i == 'novo_computador':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        #chamando func novo usuario   
        novo_computador()

    #ver pcs
    if i == 'ver_computadores':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        #chamando func novo usuario   
        ver_computadores()

    #realizar atribuição
    if i == 'nova_atribuicao':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        #chamando func novo usuario   
        nova_atribuicao()





# Menu
#NOVO USUARIO
img_new_user = Image.open('add_user.png')
img_new_user = img_new_user.resize((18,18))
img_new_user = ImageTk.PhotoImage(img_new_user)
b_new_user = Button(frameEsquerda, command=lambda:control('novo_usuario'), image=img_new_user, compound=LEFT, anchor=NW, text=" Novo Usuário", bg=co9, fg=co1, font=('Ivy 11'), activebackground= co9, overrelief=RIDGE, relief=FLAT)
b_new_user.grid(row=0,column=0,sticky=NSEW, padx=5, pady=8)

#ver usuario
img_all_users = Image.open('all_users.png')
img_all_users = img_all_users.resize((18,18))
img_all_users = ImageTk.PhotoImage(img_all_users)
b_all_users = Button(frameEsquerda, command=lambda:control('ver_usuarios'), image=img_all_users, compound=LEFT, anchor=NW, text=" Exibir todos os usuários", bg=co9, fg=co1, font=('Ivy 11'), activebackground= co9, overrelief=RIDGE, relief=FLAT)
b_all_users.grid(row=1,column=0,sticky=NSEW, padx=5, pady=8)

img_new_pc = Image.open('add_pc.png')
img_new_pc = img_new_pc.resize((18,18))
img_new_pc = ImageTk.PhotoImage(img_new_pc)
b_new_pc = Button(frameEsquerda, command=lambda:control('novo_computador'), image=img_new_pc, compound=LEFT, anchor=NW, text=" Novo Computador", bg=co9, fg=co1, font=('Ivy 11'), activebackground= co9, overrelief=RIDGE, relief=FLAT)
b_new_pc.grid(row=2,column=0,sticky=NSEW, padx=5, pady=8)

img_all_pcs = Image.open('all_pcs.png')
img_all_pcs = img_all_pcs.resize((18,18))
img_all_pcs = ImageTk.PhotoImage(img_all_pcs)
b_all_pcs = Button(frameEsquerda, command=lambda:control('ver_computadores'), image=img_all_pcs, compound=LEFT, anchor=NW, text=" Exibir todos os Computadores", bg=co9, fg=co1, font=('Ivy 11'), activebackground= co9, overrelief=RIDGE, relief=FLAT)
b_all_pcs.grid(row=3,column=0,sticky=NSEW, padx=5, pady=8)

img_assingnment = Image.open('assingnment.png')
img_assingnment = img_assingnment.resize((18,18))
img_assingnment = ImageTk.PhotoImage(img_assingnment)
b_assingnment = Button(frameEsquerda, command=lambda:control('nova_atribuicao'), image=img_assingnment, compound=LEFT, anchor=NW, text=" Atribuir um computador", bg=co9, fg=co1, font=('Ivy 11'), activebackground= co9, overrelief=RIDGE, relief=FLAT)
b_assingnment.grid(row=4,column=0,sticky=NSEW, padx=5, pady=8)

img_used_pcs = Image.open('used_pc.png')
img_used_pcs = img_used_pcs.resize((18,18))
img_used_pcs = ImageTk.PhotoImage(img_used_pcs)
b_usuario = Button(frameEsquerda, image=img_used_pcs, compound=LEFT, anchor=NW, text=" Computadores em utilização", bg=co9, fg=co1, font=('Ivy 11'), activebackground= co9, overrelief=RIDGE, relief=FLAT)
b_usuario.grid(row=5,column=0,sticky=NSEW, padx=5, pady=8)

img_trade = Image.open('update.png')
img_trade = img_trade.resize((18,18))
img_trade = ImageTk.PhotoImage(img_trade)
b_usuario = Button(frameEsquerda, image=img_trade, compound=LEFT, anchor=NW, text=" Realizar troca de equipamento", bg=co9, fg=co1, font=('Ivy 11'), activebackground= co9, overrelief=RIDGE, relief=FLAT)
b_usuario.grid(row=6,column=0,sticky=NSEW, padx=5, pady=8)

janela.mainloop()