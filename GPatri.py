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
janela.geometry ('770x330')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

# frames 
frameCima = Frame(janela, width=770, height=50, bg=co8, relief="flat")
frameCima.grid(row=0, column=0, columnspan=2, sticky=NSEW)

frameEsquerda = Frame(janela, width=150, height=265, bg=co9, relief="solid")
frameEsquerda.grid(row=1, column=0, sticky=NSEW)

frameDireita = Frame(janela, width=600, height=265, bg=co1, relief="raised")
frameDireita.grid(row=1, column=1, sticky=NSEW)

#criando divisorias "util de mais pra todo projeto"
app = Label(frameCima, width=770, height=1, padx=5, anchor=NW, font=('Verdana 1'), bg=co4, fg=co1)
app.place(x=0, y=47)

# logo 
#abrindo imagens """""importante"""""
app_img = Image.open('logo.png')
app_img = app_img.resize((40,40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, width=1000, compound=LEFT, padx=5, anchor=NW, bg=co8, fg=co1)
app_logo.place(x=5, y=0)

app = Label(frameCima, text="Sistema de Gerenciamento de Patrimonios", compound=LEFT, padx=5, anchor=NW, font=('Verdana 15 bold'), bg=co8, fg=co9)
app.place(x=50, y=7)

# Menu
#NOVO USUARIO
img_new_user = Image.open('add_user.png')
img_new_user = img_new_user.resize((18,18))
img_new_user = ImageTk.PhotoImage(img_new_user)
b_new_user = Button(frameEsquerda, image=img_new_user, compound=LEFT, anchor=NW, text=" Novo Usuário", bg=co9, fg=co1, font=('Ivy 11'), activebackground= co9, overrelief=RIDGE, relief=FLAT)
b_new_user.grid(row=0,column=0,sticky=NSEW, padx=5, pady=6)

#ver usuario
img_all_users = Image.open('all_users.png')
img_all_users = img_all_users.resize((18,18))
img_all_users = ImageTk.PhotoImage(img_all_users)
b_all_users = Button(frameEsquerda, image=img_all_users, compound=LEFT, anchor=NW, text=" Exibir todos os usuários", bg=co9, fg=co1, font=('Ivy 11'), activebackground= co9, overrelief=RIDGE, relief=FLAT)
b_all_users.grid(row=1,column=0,sticky=NSEW, padx=5, pady=6)

img_new_pc = Image.open('add_pc.png')
img_new_pc = img_new_pc.resize((18,18))
img_new_pc = ImageTk.PhotoImage(img_new_pc)
b_new_pc = Button(frameEsquerda, image=img_new_pc, compound=LEFT, anchor=NW, text=" Novo Computador", bg=co9, fg=co1, font=('Ivy 11'), activebackground= co9, overrelief=RIDGE, relief=FLAT)
b_new_pc.grid(row=2,column=0,sticky=NSEW, padx=5, pady=6)

img_all_pcs = Image.open('all_pcs.png')
img_all_pcs = img_all_pcs.resize((18,18))
img_all_pcs = ImageTk.PhotoImage(img_all_pcs)
b_all_pcs = Button(frameEsquerda, image=img_all_pcs, compound=LEFT, anchor=NW, text=" Exibir todos os Computadores", bg=co9, fg=co1, font=('Ivy 11'), activebackground= co9, overrelief=RIDGE, relief=FLAT)
b_all_pcs.grid(row=3,column=0,sticky=NSEW, padx=5, pady=6)

img_assingnment = Image.open('assingnment.png')
img_assingnment = img_assingnment.resize((18,18))
img_assingnment = ImageTk.PhotoImage(img_assingnment)
b_assingnment = Button(frameEsquerda, image=img_assingnment, compound=LEFT, anchor=NW, text=" Atribuir um computador", bg=co9, fg=co1, font=('Ivy 11'), activebackground= co9, overrelief=RIDGE, relief=FLAT)
b_assingnment.grid(row=4,column=0,sticky=NSEW, padx=5, pady=6)

img_used_pcs = Image.open('used_pc.png')
img_used_pcs = img_used_pcs.resize((18,18))
img_used_pcs = ImageTk.PhotoImage(img_used_pcs)
b_usuario = Button(frameEsquerda, image=img_used_pcs, compound=LEFT, anchor=NW, text=" Computadores em utilização", bg=co9, fg=co1, font=('Ivy 11'), activebackground= co9, overrelief=RIDGE, relief=FLAT)
b_usuario.grid(row=5,column=0,sticky=NSEW, padx=5, pady=6)

img_trade = Image.open('update.png')
img_trade = img_trade.resize((18,18))
img_trade = ImageTk.PhotoImage(img_trade)
b_usuario = Button(frameEsquerda, image=img_trade, compound=LEFT, anchor=NW, text=" Realizar troca de equipamento", bg=co9, fg=co1, font=('Ivy 11'), activebackground= co9, overrelief=RIDGE, relief=FLAT)
b_usuario.grid(row=6,column=0,sticky=NSEW, padx=5, pady=6)

janela.mainloop()