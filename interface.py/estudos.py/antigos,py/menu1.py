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

barrademenu=Menu(Janela)#adivinhaa

menucomtatos=Menu(barrademenu,tearoff=0)#opicao do menu 

menucomtatos.add_command(label="novo",command=novocontato)
menucomtatos.add_command(label="pesquisa",command=semcomando)
menucomtatos.add_command(label="deletar",command=semcomando)
menucomtatos.add_separator()#separacao 
menucomtatos.add_command(label="fechar",command=Janela.quit)#fechara a janela
barrademenu.add_cascade(label="contados",menu=menucomtatos)#acrecentando na funcao barramenu(importante)

menumanutencao=Menu(barrademenu,tearoff=0)
menumanutencao.add_command(label="Banco de dados",command=semcomando)
barrademenu.add_cascade(label="manutencao",menu=menumanutencao)

menusobre=Menu(barrademenu,tearoff=0)
menusobre.add_command(label="cfb",command=semcomando)
barrademenu.add_cascade(label="sobre",menu=menusobre)#nao se esqueca desse menu(menu=)

Janela.config(menu=barrademenu)
Janela.mainloop()