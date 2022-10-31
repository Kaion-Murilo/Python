import os
from tkinter import *

if os.name == "nt":
    os.system("cls");

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

Janela = Tk()
Janela.title("Aula de Interface - 27/05/22")
Janela.geometry("400x300")
Janela.configure(background="#55626b")

Texto_1 = Label(Janela, text="Aula 1 de Interface Gráfica - 27/05/2055", background="#d16704", foreground="#fa05d9")
Texto_1.place(x=10, y=20, width=250, height=20)

teste = "Utilizando o TKinter!"
cor_bg = "#fff"
cor_fg = "#689"
Texto_2 = Label(Janela, text= teste, background=cor_bg, foreground=cor_fg)
Texto_2.place(x=10, y=45, width=250, height=20)

Texto_3 = Label(Janela, text="Nome", background="#fff", foreground="#000")
Texto_3.place(x=20, y=70, width=70, height=30)
Nome = Entry(Janela)
Nome.place(x=90, y=70, width=200, height=30)

Texto_4 = Label(Janela, text="Idade", background="#fff", foreground="#000")
Texto_4.place(x=20, y=105, width=70, height=30)
Idade = Entry(Janela)
Idade.place(x=90, y=105, width=200, height=30)

Texto_5 = Label(Janela, text="Observações", background="#fff", foreground="#000")
Texto_5.place(x=20, y=140, width=100, height=30)
Obs_p = Text(Janela)
Obs_p.place(x=20, y=170, width=200, height=80)

Botao_1 = Button(Janela, text="Pegar Dados!", command=Pegar_Dados, background="#00f", foreground="#fff")
Botao_1.place(x=70, y=260, width=70, height=30)

Texto_6 = Label(Janela, text="", background="#fff", foreground="#000")
Texto_6.place(x=300, y=80, width=200, height=30)

Janela.mainloop()