from asyncore import write
import email
from optparse import Values
import os
from tkinter import *
import os
# adicionar arqquivo txt
c=os.path.dirname(__file__)
nomeArquivo=c+"\\nome.txt"
# continua no def mostrarcarrinho
if os.name == "nt":
    os.system("cls");

def gravardados():
    if Nome.get() != "":
        vnome= Nome.get();
        vidade = Idade.get();
        vemail = Obs_p.get("1.0",END);
        vquery="INSERT INTO nome (nome,idade,email)VALUES ('"+vnome+"','"+vidade+"','"+vemail+"')"
        print(vquery)
        bamco.dml(vquery)
        # Nome.delete(0,END)
        # Idade.delete(0,END)
        # Obs_p.delete("1.0",END)
        print("gravar dados executada")
    else:
        print("erro graava erro")

def Pegar_Dados():
    Nome_inf = Nome.get();
    Idade_inf = Idade.get();
    Obs_inf = Obs_p.get("1.0",END);
    print(f"Nome: {Nome_inf}")
    print(f"Idade: {Idade_inf}")
    print(f"Observações:\n{Obs_inf}")
    Texto_6["text"] = Nome_inf
    Nome.delete(0,END)
    Idade.delete(0,END)
    Obs_p.delete("1.0",END)
def armazenar():
    arquivo=open(nomeArquivo,"a")
    arquivo.write("   nome....:%s"%  Nome.get())
    arquivo.write("\n idade...:%s"%  Idade.get())
    arquivo.write("\n email...:%s"%  email.get()) 
    arquivo.write("\n obs....:%s"%    Obs_p.get("1.0",END))           
    arquivo.write("\n\n") 
    arquivo.close  
def mostrarcarrinho():
     arquivo = open(nomeArquivo, 'r')
     conteudo = arquivo.readlines()
     Texto_8["text"]=conteudo
     []
     arquivo.close              
Janela = Tk()
Janela.title("interface - mangar")
Janela.geometry("700x500")
Janela.configure(background="#55626b")
preto="#00000d"
vermelgo="#e01212"
azul="#1e363b"
braco="#fafeff"
verde="#13872a"
Texto_1 = Label(Janela, text="Interface ", background=braco, foreground=preto)
Texto_1.place(x=200, y=20, width=250, height=20)
teste = "cadatro"
cor_bg = "#fff"  #
cor_fg = "#689"
Texto_2 = Label(Janela, text= teste, background=cor_bg, foreground=cor_fg)
Texto_2.place(x=20, y=45, width=250, height=20)

Texto_3 = Label(Janela, text="Nome", background="#fff", foreground="#000",anchor=W)
Texto_3.place(x=20, y=70, width=70, height=30)

Nome = Entry(Janela)
Nome.place(x=90, y=70, width=200, height=30)

Texto_4 = Label(Janela, text="Idade", background="#fff", foreground="#000",anchor=W)
Texto_4.place(x=20, y=105, width=70, height=30)

Idade = Entry(Janela)
Idade.place(x=90, y=105, width=200, height=30)

Texto_5 = Label(Janela, text="Observações", background="#fff", foreground="#000",anchor=W)
Texto_5.place(x=20, y=140, width=100, height=30)

Obs_p = Text(Janela)
Obs_p.place(x=20, y=170, width=200, height=80)

Botao_1 = Button(Janela, text="imprimir", command=Pegar_Dados, background="#00f", foreground="#fff")
Botao_1.place(x=20, y=260, width=70, height=30)

Texto_6 = Label(Janela, text="", background="#fff", foreground="#000")
Texto_6.place(x=300, y=70, width=200, height=30)

Botao_1 = Button(Janela, text="Salvar", command=armazenar, background=verde, foreground=preto,)
Botao_1.place(x=180, y=260, width=100, height=30)

Texto_7 = Label(Janela, text="email", background="#fff", foreground="#000",anchor=W)
Texto_7.place(x=300, y=105, width=60, height=30)
email = Entry(Janela)
email.place(x=350, y=105, width=200, height=30)

Botao_3 = Button(Janela, text="print", command=mostrarcarrinho, background="#00f", foreground="#fff")
Botao_3.place(x=279, y=260, width=70, height=30)

Texto_8 = Label(Janela, text="", background="#fff", foreground="#000")
Texto_8.place(x=600, y=80, width=400, height=470)

Botao_3 = Button(Janela, text="gravar dados", command=gravardados, background="#00f", foreground="#fff")
Botao_3.place(x=380, y=360, width=80, height=60)
Janela.mainloop()