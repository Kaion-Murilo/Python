from cProfile import label
import os
from tkinter import *
pastainterface=os.path.dirname(__file__)
def semcomando():#funcao teste
    print("oi")

def novocontato():#entrar em outro formulario
    exec(open(pastainterface+"\\interface.py").read())
    
    
Janela = Tk()
Janela.title("interface - mangar")
Janela.geometry("700x500")
Janela.configure(background="#55626b")

imag=PhotoImage(file="cpf/logo.png.png")
label_imagen=Label(Janela,image=imag).pack()

Janela.mainloop()