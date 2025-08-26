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

janela.mainloop()