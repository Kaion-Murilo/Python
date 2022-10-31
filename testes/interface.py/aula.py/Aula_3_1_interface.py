import os
from tkinter import * 

if os.name == "nt":
    os.system("cls");

class Nova_Tela:
    def __init__(self, janela):
        self.Janela = janela
        self.Tela() #chamada da Função
        self.Frames_Tela()
        self.Botoes_Tela()
    
    def Tela(self):#tela principal
        self.Janela.title("Aula 03/06/2022")
        self.Janela.configure(background="#777")
        self.Janela.geometry("700x500")
        self.Janela.resizable(True, True)
        self.Janela.maxsize(width=800, height=600)
        self.Janela.minsize(width=600, height=400)

    def Frames_Tela(self):#janelas ou setores dentro da tela princiapal
        self.Frame_1 = Frame(self.Janela, bg="#f00",
                            highlightbackground="#fff",
                            highlightthickness=4)#borda do frame 
        self.Frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, 
                            relheight=0.46)
        self.Frame_2 = Frame(self.Janela, bg="#00f",
                            highlightbackground="#0f0",
                            highlightthickness=2)
        self.Frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, 
                            relheight=0.46)#relx=x mais em porcentagem  tudo por poecentagem

    def Botoes_Tela(self):#butoes
        self.Botao_1 = Button(self.Frame_1)#localizacao para seus parametros
        self.Botao_1["text"] = "Fechar"
        self.Botao_1["font"] = ("Arial", "12", "bold")#especificacoe do texto
        self.Botao_1["command"] = quit
        self.Botao_1.place(relx=0.2, rely=0.1, 
                           relwidth=0.1, relheight=0.15)

        self.Botao_2 = Button(self.Frame_2)
        self.Botao_2["text"] = "Teste"
        self.Botao_2["font"] = ("Arial", "12", "italic")
        self.Botao_2["command"] = self.Nova_Janela
        self.Botao_2.place(relx=0.2, rely=0.1, 
                           relwidth=0.1, relheight=0.15)

    def Nova_Janela(self):#criar nova janela 
        self.Janela_2 = Toplevel()
        self.Janela_2.title("Nova Janela")
        self.Janela_2.geometry("300x300")
        self.Janela_2.configure(background="#000")
        self.Janela_2.resizable(False, False)
        self.Janela_2.transient(self.Janela)
        self.Janela_2.focus_force()
        self.Janela_2.grab_set()

Janela = Tk()
Nova_Tela(Janela)
Janela.mainloop()