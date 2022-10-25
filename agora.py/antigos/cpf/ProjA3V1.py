import os
os.system('cls')
import cpf1
from tkinter import * 

        #### Chamada das funcões e criação da interface ####

class Interface_LocBoy:
    def __init__(self, janela):
        self.Janela = janela
        self.Tela()
        self.Frames_Tela()
        self.Botoes_Tela()
           
        #### Janela principal ####
    def Tela(self):
        self.Janela.title("LocBoy")
        self.Janela.configure(background="#9370DB")
        self.Janela.geometry("800x600")
        self.Janela.resizable(True, True)
        self.Janela.maxsize(width=1800, height=1000)
        self.Janela.minsize(width=600, height=400)

        #### Frames do titulo, login e marca da academia da tela inicial####

    def Frames_Tela(self):
        self.Frame_1 = Frame(self.Janela, bg="#00FF00",
                            highlightbackground="#fff",
                            highlightthickness=4)
        self.Frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.185)
        self.Texto_1 = Label(self.Frame_1, text="Academia LocBoy",
                                             background="#00FF00", 
                                             foreground="#0000FF", 
                                             font="Gotham 60")
        self.Texto_1.place(relx=0.02, rely=0.002, relwidth=0.96, relheight=1)
        self.Frame_2 = Frame(self.Janela, bg="#00FF00",
                            highlightbackground="#fff",
                            highlightthickness=2)
        self.Frame_2.place(relx=0.02, rely=0.40, relwidth=0.42, relheight=0.45)
        self.Texto_2 = Label(self.Frame_2, text="USUÁRIO:",
                                             background="#FFFFFF", 
                                             foreground="#0000FF", 
                                             font="Arialblack 17")
        self.Texto_2.place(relx=0.04, rely=0.08, relwidth=0.42, relheight=0.2)
        self.Nome = Entry(self.Frame_2)
        self.Nome.place(relx=0.5, rely=0.08, relwidth=0.45, relheight=0.2)
        self.Texto_3 = Label(self.Frame_2, text="SENHA:",
                                             background="#FFFFFF", 
                                             foreground="#0000FF", 
                                             font="Arialblack 17")
        self.Texto_3.place(relx=0.04, rely=0.33, relwidth=0.42, relheight=0.2)
        self.Nome = Entry(self.Frame_2)
        self.Nome.place(relx=0.5, rely=0.33, relwidth=0.45, relheight=0.2)
        self.Frame_3 = Frame(self.Janela, bg="#00FF00",
                            highlightbackground="#fff",
                            highlightthickness=2)
        self.Frame_3.place(relx=0.460, rely=0.3, relwidth=0.52, relheight=0.66)       

        #### Botões da tela inicial ####

    def Botoes_Tela(self):
        self.Botao_1 = Button(self.Frame_2)
        self.Botao_1["text"] = "Entrar"
        self.Botao_1["font"] = ("Arial", "25", "bold")
        self.Botao_1["command"] = self.Janela_Usuario
        self.Botao_1.place(relx=0.04, rely=0.6, relwidth=0.91, relheight=0.15)
        self.Botao_2 = Button(self.Frame_2)
        self.Botao_2["text"] = "Cadastrar"
        self.Botao_2["font"] = ("Arial", "20", "bold")
        self.Botao_2["command"] = self.Janela_Tipo_Usuario
        self.Botao_2.place(relx=0.04, rely=0.78, relwidth=0.91, relheight=0.15)

        

        #### NovasJanelas ####
     
    def Janela_Usuario(self):
        self.Janela_2 = Toplevel()
        self.Janela_2.title("Usuário")
        self.Janela_2.geometry("800x600")
        self.Janela_2.configure(background="#00FF00")
        self.Janela_2.resizable(True, True)
        self.Janela.maxsize(width=1800, height=1000)
        self.Janela.minsize(width=600, height=400)
        self.Janela_2.focus_force()
        self.Janela_2.grab_set()
        self.Frame_4 = Frame(self.Janela_2, bg="#9370DB",
                            highlightbackground="#fff",
                            highlightthickness=4)
        self.Frame_4.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.185)
        self.Texto_4 = Label(self.Frame_4, text="Academia LocBoy",
                                             background="#9370DB", 
                                             foreground="#FFFFFF", 
                                             font="Gotham 60")
        self.Texto_4.place(relx=0.02, rely=0.002, relwidth=0.96, relheight=1)

    def Janela_Tipo_Usuario(self):
        self.Janela_3 = Toplevel()
        self.Janela_3.title("Cadastro")
        self.Janela_3.geometry("300x400")
        self.Janela_3.configure(background="#FF7F00")
        self.Janela_3.resizable(False, False)
        self.Janela.maxsize(width=1800, height=1000)
        self.Janela.minsize(width=600, height=400)
        self.Janela_3.focus_force()
        self.Janela_3.grab_set()
        self.Frame_5 = Frame(self.Janela_3, bg="#9370DB",
                            highlightbackground="#fff",
                            highlightthickness=4)
        self.Frame_5.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.185)
        self.Texto_5 = Label(self.Frame_5, text="Academia LocBoy",
                                             background="#9370DB", 
                                             foreground="#00FF00", 
                                             font="Gotham 20")
        self.Texto_5.place(relx=0.02, rely=0.002, relwidth=0.96, relheight=1)
        self.Frame_6 = Frame(self.Janela_3, bg="#9370DB",
                            highlightbackground="#fff",
                            highlightthickness=4)
        self.Frame_6.place(relx=0.02, rely=0.25, relwidth=0.96, relheight=0.70)
        self.Texto_6 = Label(self.Frame_6, text="ESCOLHA UM USUÁRIO:")
        self.Texto_6["font"] = ("Arial", "14", "bold","italic")
        self.Texto_6["background"]="#fff" 
        self.Texto_6["foreground"]="#000"
        self.Texto_6.place(relx=0.01, rely=0.02, relwidth=0.98, relheight=0.2)


        #### BOTÕES PARA ESCOLHER O TIPO DE CADASTRO DE USUÁRIO####

        self.Botao_3 = Button(self.Frame_6)
        self.Botao_3["text"] = "Funcionário"
        self.Botao_3["font"] = ("Arial", "14", "bold","italic")
        self.Botao_3["command"] = self.Janela_Cadastro_Funcionário
        self.Botao_3.place(relx=0.01, rely=0.26, relwidth=0.98, relheight=0.16)

        self.Botao_4 = Button(self.Frame_6)
        self.Botao_4["text"] = "Aluno"
        self.Botao_4["font"] = ("Arial", "14", "bold","italic")
        self.Botao_4["command"] = self.Janela_Cadastro_Aluno
        self.Botao_4.place(relx=0.01, rely=0.44, relwidth=0.98, relheight=0.16)

        self.Botao_5 = Button(self.Frame_6)
        self.Botao_5["text"] = "Professor"
        self.Botao_5["font"] = ("Arial", "14", "bold","italic")
        self.Botao_5["command"] = self.Janela_Cadastro_Professor
        self.Botao_5.place(relx=0.01, rely=0.62, relwidth=0.98, relheight=0.16)

        self.Botao_6 = Button(self.Frame_6)
        self.Botao_6["text"] = "Convidado"
        self.Botao_6["font"] = ("Arial", "14", "bold","italic")
        self.Botao_6["command"] = self.Janela_Cadastro_Convidado
        self.Botao_6.place(relx=0.01, rely=0.80, relwidth=0.98, relheight=0.16)

        #### Janelas de cadastro dos diferentes tipos de usuário ####

    def Janela_Cadastro_Funcionário(self):
        self.Janela_3.destroy()
        self.Janela_4 = Toplevel()
        self.Janela_4.title("Cadastro de Funcionário")
        self.Janela_4.geometry("800x600")
        self.Janela_4.configure(background="#FF7F00")
        self.Janela_4.resizable(True, True)
        self.Janela.maxsize(width=1800, height=1000)
        self.Janela.minsize(width=600, height=400)
        self.Janela_4.focus_force()
        self.Janela_4.grab_set()
        self.Frame_7 = Frame(self.Janela_4, bg="#00FF00",highlightbackground="#fff",highlightthickness=4)
        self.Frame_7.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.12)
        self.Texto_7 = Label(self.Frame_7, text="Academia LocBoy",
                                             background="#00FF00", 
                                             foreground="#0000FF", 
                                             font="Gotham 30")
        self.Texto_7.place(relx=0.02, rely=0.002, relwidth=0.96, relheight=1)
        self.Frame_8 = Frame(self.Janela_4, bg="#00FF00",
                            highlightbackground="#fff",
                            highlightthickness=2)
        self.Frame_8.place(relx=0.02, rely=0.185, relwidth=0.96, relheight=0.77)
        self.Frame_9 = Frame(self.Janela_4, bg="#FFFFFF",
                            highlightbackground="#fff",
                            highlightthickness=2)
        self.Frame_9.place(relx=0.78, rely=0.205, relwidth=0.185, relheight=0.25)
        self.Texto_8 = Label(self.Frame_8, text="Nome:")
        self.Texto_8["background"]="#dde"
        self.Texto_8["foreground"]="#00f" 
        self.Texto_8["anchor"] = W
        self.Texto_8.place(relx=0.025, rely=0.025, relwidth=0.1, relheight=0.065)
        self.Nome = Entry(self.Frame_8)
        self.Nome.place(relx=0.135, rely=0.025, relwidth=0.35, relheight=0.065)
        self.Texto_9 = Label(self.Frame_8, text="Cpf:")
        self.Texto_9["background"]="#dde"
        self.Texto_9["foreground"]="#00f" 
        self.Texto_9["anchor"] = W
        self.Texto_9.place(relx=0.025, rely=0.105, relwidth=0.1, relheight=0.065)
        self.Cpf = Entry(self.Frame_8)
        self.Cpf.place(relx=0.135, rely=0.105, relwidth=0.35, relheight=0.065)
        self.Texto_10 = Label(self.Frame_8, text="Email:")
        self.Texto_10["background"]="#dde"
        self.Texto_10["foreground"]="#00f" 
        self.Texto_10["anchor"] = W
        self.Texto_10.place(relx=0.025, rely=0.185, relwidth=0.1, relheight=0.065)
        self.Email = Entry(self.Frame_8)
        self.Email.place(relx=0.135, rely=0.185, relwidth=0.35, relheight=0.065)
        self.Texto_11 = Label(self.Frame_8, text="Tel:")
        self.Texto_11["background"]="#dde"
        self.Texto_11["foreground"]="#00f" 
        self.Texto_11["anchor"] = W
        self.Texto_11.place(relx=0.025, rely=0.270, relwidth=0.1, relheight=0.065)
        self.Tel = Entry(self.Frame_8)
        self.Tel.place(relx=0.135, rely=0.270, relwidth=0.35, relheight=0.065)
        self.Texto_12 = Label(self.Frame_8, text="Senha:")
        self.Texto_12["background"]="#dde"
        self.Texto_12["foreground"]="#00f" 
        self.Texto_12["anchor"] = W
        self.Texto_12.place(relx=0.025, rely=0.355, relwidth=0.1, relheight=0.065)
        self.Senha = Entry(self.Frame_8)
        self.Senha.place(relx=0.135, rely=0.355, relwidth=0.35, relheight=0.065)
        self.Botao_7 = Button(self.Frame_8, text="Salvar")
        self.Botao_7["font"] = ("Calibri", "10")
        self.Botao_7["command"] = self.validacao
        self.Botao_7["background"]="#0000FF" 
        self.Botao_7["foreground"]="#000"
        
        self.Botao_7.place(relx=0.135, rely=0.555, relwidth=0.35, relheight=0.065)
        


    def Janela_Cadastro_Aluno(self):
        self.Janela_3.destroy()
        self.Janela_5 = Toplevel()
        self.Janela_5.title("Cadastro de Alunos")
        self.Janela_5.geometry("800x600")
        self.Janela_5.configure(background="#FF7F00")
        self.Janela_5.resizable(True, True)
        self.Janela.maxsize(width=1800, height=1000)
        self.Janela.minsize(width=600, height=400)
        self.Janela_5.focus_force()
        self.Janela_5.grab_set()

    def Janela_Cadastro_Professor(self):
        self.Janela_3.destroy()
        self.Janela_6 = Toplevel()
        self.Janela_6.title("Cadastro de Professores")
        self.Janela_6.geometry("800x600")
        self.Janela_6.configure(background="#FF7F00")
        self.Janela_6.resizable(True, True)
        self.Janela.maxsize(width=1800, height=1000)
        self.Janela.minsize(width=600, height=400)
        self.Janela_6.focus_force()
        self.Janela_6.grab_set()

    def Janela_Cadastro_Convidado(self):
        self.Janela_3.destroy()
        self.Janela_7 = Toplevel()
        self.Janela_7.title("Cadastro de Convidados")
        self.Janela_7.geometry("800x600")
        self.Janela_7.configure(background="#FF7F00")
        self.Janela_7.resizable(True, True)
        self.Janela.maxsize(width=1800, height=1000)
        self.Janela.minsize(width=600, height=400)
        self.Janela_7.focus_force()
        self.Janela_7.grab_set()

    
        
              

Janela = Tk()
Interface_LocBoy(Janela)
Janela.mainloop()