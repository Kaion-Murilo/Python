import os
import sqlite3
from sqlite3 import Error
from tkinter import END, filedialog
from tkinter.ttk import Treeview
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
if os.name=="nt":
    os.system("cls");
import re       
class validacpf:#validação de cpf
    def __init__(self,cpf):
        self.cpf=cpf
        
        self.cpf=cpf
        self.valida()
    def valida(self):#funcão principal
        if not self.cpf: 
            print("caio")
            return False
        novo_cpf=self._calcula_digito(self.cpf[:9])  
        novo_cpf=self._calcula_digito(novo_cpf)
        #529.982.247-25
        a=0
        if novo_cpf==self.cpf:
            print (" valida 1")
            return  True
        else:
            print ("nao valida 1")
        
            return False
        
    @staticmethod
    def _calcula_digito(fatia_cpf):#calculo
        print("02")
        if not fatia_cpf:
            
            return False
        sequencia=fatia_cpf[0]*len(fatia_cpf)
        print(sequencia)
        if sequencia == fatia_cpf:
            return False    
        print("cauculo")
        soma=0
        for chave,multiplicador in enumerate(range(len(fatia_cpf)+1,1,-1)):
            soma += int(fatia_cpf[chave])* multiplicador
        print(soma)
        resto=11-(soma%11)
        resto=resto if resto <=9 else 0
        return fatia_cpf + str(resto)
    @property
    def cpf(self):#decorador
        print("1")
        return self._cpf
    
    @cpf.setter
    def cpf (self,cpf):#setter no cpf
        print("2")
        self._cpf=self._so_numeros(cpf)
           
    @staticmethod
    def _so_numeros(cpf):#3
        print("3")
        print(cpf)
        return re.sub('[^0-9]', '', cpf)#Revisão e substituição de caracteres desnecessário.
class pessoa:
        def __init__(self,email,nome,numero,idade,senha,plano,cpf,salario,):
            self.email=email
            print(f"email={self.email}")
            self.nome=nome
            print(f"nome={self.nome}")
            self.numero=numero
            print(f"telefone={self.numero}")
            self.idade=idade
            print(f"idade={self.idade}")
            self.senha=senha
            print(f"senha={self.senha}")
            self.plano=plano
            print(f"plano={self.plano}")
            self.cpf=cpf
            print(f"cpf={self.cpf}")
            self.salario=salario
            print (f"salario={self.salario}")            
class aluno:
    def __init__(self,email,nome,numero,idade,senha,plano,cpf):
        self.email=email
        print(f"email={self.email}")
        self.nome=nome
        print(f"nome={self.nome}")
        self.numero=numero
        print(f"telefone={self.numero}")
        self.idade=idade
        print(f"idade={self.idade}")
        self.senha=senha
        print(f"senha={self.senha}")
        self.plano=plano
        print(f"plano={self.plano}")
        self.cpf=cpf
        print(f"cpf={self.cpf}")
        self.us="aluno"
class funcionario:
    def __init__(self,email,nome,numero,senha,cpf,salario):
        self.email=email
        print(f"email={self.email}")
        self.nome=nome
        print(f"nome={self.nome}")
        self.numero=numero
        print(f"numero={self.numero}")
        self.senha=senha
        print(f"salario={self.senha}")
        self.cpf=cpf
        print(f"cpf={self.cpf}")   
        self.salario=salario
        print (f"cpf={self.salario}")  
        self.us="funcionario" 
class convidado:
        def __init__(self,nome,numero):
            self.nome=nome
            print(f"nome={self.nome}")
            self.numero=numero
            print(f"numero={self.numero}")
            self.us="convidado"
class Funcoes_BD():
    def Conexao_BD (self):
        caminho_BD ="banco_1_.db"
        self.conex_banco = None
        try:
            self.conex_banco =sqlite3.connect(caminho_BD)
            self.cursor=self.conex_banco.cursor()
            print("Conexão com o banco Dados efetuada com Sucesso!")
        except Error as erro:
            print("Houve algum erro com a comunicação com o BD: ", erro)
    def desconectaBD(self):
        self.conex_banco.close()
        print("banco de Dados Desconectadol?")
    def alterar_BD_aluno(self):
        self.pegar_dados_pessoa()  
        self.Conexao_BD()
        Comando = f"""UPDATE pessoa SET nome='{self.Liv.nome}',
        idade={self.Liv.idade},email='{self.Liv.email}',
        plano='{self.Liv.plano}',senha='{self.Liv.senha}',
        cpf={self.Liv.cpf},numero={self.Liv.numero} where cpf='{self.Liv.cpf}' """
        
        self.cursor.execute(Comando)
        self.conex_banco.commit()
        print("elemento alterado com sucesso")
        self.desconectaBD()
        self.Limpar_Campos_geral()
    def alterar_BD_Com(self):
        self.pegar_dados_pessoa()  
        self.Conexao_BD()
        Comando = f"""UPDATE pessoa SET nome='{self.Liv.nome}',
        numero={self.Liv.numero} where numero='{self.Liv.numero} '"""
        self.cursor.execute(Comando)
        self.conex_banco.commit()
        print("elemento alterado com sucesso")
        self.desconectaBD()
        self.Limpar_Campos_geral()
    def alterar_BD_Prof(self):
        self.pegar_dados_pessoa()  
        self.Conexao_BD()
        Comando = f"""UPDATE pessoa SET nome ='{self.Liv.nome}',
        cpf='{self.Liv.cpf}',email='{self.Liv.email}',
        numero={self.Liv.numero},
        senha='{self.Liv.senha}',salario={self.Liv.salario}
        where cpf='{self.Liv.cpf}' """
        self.cursor.execute(Comando)
        self.conex_banco.commit()
        print("elemento alterado com sucesso")
        self.desconectaBD()
        self.Limpar_Campos_geral()
    def alterar_BD_Func(self):
        self.pegar_dados_pessoa()  
        self.Conexao_BD()
        self.us='funcionario'
        Comando = f"""UPDATE pessoa SET nome ='{self.Liv.nome}',
        cpf='{self.Liv.cpf}',email='{self.Liv.email}',numero={self.Liv.numero},
        senha='{self.Liv.senha}',salario={self.Liv.salario} where cpf='{self.Liv.cpf}' """
        self.cursor.execute(Comando)
        self.conex_banco.commit()
        print("elemento alterado com sucesso")
        self.desconectaBD()
        self.Limpar_Campos_geral()
    def Exclui_BD_alu(self):
        self.pegar_dados_pessoa()
        self.Conexao_BD()
        Comando= f"""DELETE FROM pessoa WHERE  nome= '{self.Liv.nome}' """
        self.cursor.execute(Comando)
        self.conex_banco.commit()
        print("Elemento excluido com Sucesso!")
        self.desconectaBD()
        self.Limpar_Campos_geral()   
    
        self.pegar_dados_pessoa()
        self.Conexao_BD()
        Comando= f"""DELETE FROM convidado WHERE numero='{self.Liv.numero}' """
        self.cursor.execute(Comando)
        self.conex_banco.commit()
        print("Elemento excluido com Sucesso!")
        self.desconectaBD()
        self.Limpar_Campos_geral()    
    def Atualizar_Listagem_BD_Alu(self):
        self.tv.delete(*self.tv.get_children())
        self.Conexao_BD()
        Lista = self.cursor.execute("""SELECT id,nome,numero,idade,senha,email,cpf,salario,plano,usuario FROM pessoa ORDER BY ID ASC;""")
        for i in Lista:
            self.tv.insert("",END,values=i)
        self.desconectaBD()
    def Cadastrar_BD_alu(self):
        self.Pega_dados_alu()
        self.Conexao_BD() 
        self.cursor.execute(f"""INSERT INTO pessoa(nome,usuario,email,numero,idade,senha,cpf,plano) VALUES 
        ('{self.Liv.nome}','{self.Liv.us}',{self.Liv.numero},{self.Liv.idade},{self.Liv.email},
        '{self.Liv.cpf}','{self.Liv.senha}','{self.Liv.plano}')""")
        self.conex_banco.commit();
        self.desconectaBD()
    def Cadastrar_BD_Prof(self):
        self.Pega_dados_prof()
        self.Liv.us="profesor"
        self.Conexao_BD() 
        self.cursor.execute(f"""INSERT INTO Pessoa(nome,numero,usuario,senha,email,cpf,salario) VALUES ('{self.Liv.nome}',{self.Liv.numero},'{self.Liv.us}',
        '{self.Liv.senha}','{self.Liv.email}','{self.Liv.cpf}',{self.Liv.salario}) """)
        self.conex_banco.commit();
        self.desconectaBD()
        # self.Limpar_Campos()   
    def Cadastrar_BD_func(self):
        self.Pega_dados_func()
        self.Conexao_BD() 
        print("passou")
        self.cursor.execute(f"""INSERT INTO pessoa(nome,numero,senha,usuario,email,cpf,salario) VALUES 
        ('{self.Liv.nome}',{self.Liv.numero},'{self.Liv.senha}','{self.Liv.us}',
        '{self.Liv.email}','{self.Liv.cpf}',{self.Liv.salario})""")
        print("deixou")
        self.conex_banco.commit();
        self.desconectaBD()
        # self.Limpar_Campos()   
    def Cadastrar_BD_Com(self):
        self.Pega_dados_Com()
        self.Conexao_BD() 
        self.cursor.execute(f"""INSERT INTO pessoa(nome,numero,usuario) VALUES('{self.Liv.nome}',{self.Liv.numero},'{self.Liv.us}') """)
        self.conex_banco.commit();
        self.desconectaBD()
    def Pega_dados_Com(self): 
        self.Liv = convidado(nome= self.Nome_Con.get() ,numero=self.Tel_Con.get())
    def Pega_dados_func(self): 
        self.Liv = funcionario(nome=self.Nome_Fun.get() ,cpf= self.Cpf_Fun.get(),numero= self.Tel_Fun.get(),
                              salario=self.Salario_Fun.get(),
                               senha=self.Senha_Fun.get(),email=self.Email_Fun.get() ) 
    def pegar_dados_pessoa(self):
        self.Liv = pessoa(nome=self.Nome_T_Usuario.get() ,cpf=self.vcpf.get(),numero= self.vfone.get(),
                         idade=self.vidade.get() ,senha=self.vsenha.get() ,email=self.vemail.get(),
                         plano=self.vplano.get(),salario=self.vsalario.get())
    def Pega_dados_prof(self): 
        self.Liv = funcionario(nome=self.Nome_Prof.get(),cpf=self.Cpf_Prof.get(),
                               numero= self.Tel_Prof.get() ,salario=float(self.Salario_Prof.get()) ,
                               senha=self.Senha_Prof.get(),email= self.Email_Prof.get()) 
    def Pega_dados_alu(self): 
        self.Liv = aluno(nome=self.Nome_Alu.get() ,cpf=self.Cpf_Alu.get() ,numero= self.Tel_Alu.get(),
                         idade=int(self.Idade_Alu.get()) ,senha=self.Senha_Alu.get() ,email=self.Email_Alu.get(),
                         plano=self.V_Plano.get())
    def Criar_Tabela_BD(self):
        try: 
            self.Conexao_BD()
            Comando="""CREATE TABLE IF NOT EXISTS aluno(ID INTEGER PRIMARY KEY AUTOINCREMENT,nome VARCHAR (100),
            email VARCHAR(30) not null,
            CPF VARCHAR(30) NOT NULL,
            numero integer ,
            idade intege,
            plano VARCHAR(0),
            senha VARCHAR(30));"""
            comando1="""CREATE TABLE IF NOT EXISTS funcionario(ID INTEGER PRIMARY KEY AUTOINCREMENT,nome VARCHAR (100),
            email varchar(100) not null,
            CPF VARCHAR(30) NOT NULL,
            numero integer ,
            senha VARCHAR(30),
            salario integer );"""
            comando2="""CREATE TABLE IF NOT EXISTS Profesor(ID INTEGER PRIMARY KEY AUTOINCREMENT,nome VARCHAR (100),
            email varchar(100) not null,
            CPF VARCHAR(30) NOT NULL,
            numero integer ,
            senha VARCHAR(30),
            salario integer );"""
            comando3="""CREATE TABLE IF NOT EXISTS Convidado(ID INTEGER PRIMARY KEY AUTOINCREMENT,nome VARCHAR (100),numero integer);"""
            
            self.cursor.execute(Comando)
            self.cursor.execute(comando1)
            self.cursor.execute(comando2)
            self.cursor.execute(comando3)
            
            self.conex_banco.commit()
            print("Tabelas Criadas com Sucesso!") 
            self.desconectaBD() 
        except Error as erros:
            print("Criação de TABELAS FALHOU: ", erros)

        self.vsenha.delete(0,END,)
    def Limpar_Campos_geral(self):
            self.vsalario.delete(0,END)
            self.vplano.delete(0,END);
            self.Nome_T_Usuario.delete(0,END); 
            self.vidade.delete (0,END);
            self.vemail.delete(0,END);
            self.vsenha.delete(0,END);
            self.vfone.delete(0,END,);
            self.vcpf.delete(0,END);
    def clique_duplo(self, event):
        self.Limpar_Campos_geral() 
        self.tv.selection()
        print("oi")
        for m in self.tv.selection():
            id,nome,numero,idade,senha,email,cpf,salario,plano,usuario = self.tv.item(m,'values')
            self.vsalario.insert(END,salario)
            # self.vplano.insert(END,plano);
            self.Nome_T_Usuario.insert(END,nome); 
            self.vidade.insert (END,idade);
            self.vemail.insert(END,email);
            self.vsenha.insert(END,senha);
            self.vfone.insert(END,numero);
            self.vcpf.insert(END,cpf);

Lista_Plano = ["Plano Básico", "Plano Médio", "Plano Completo"]
Lista_Usuario = ["Funcionário", "Professor", "Aluno", "Convidado"]

        #### Chamada das funcões e criação da interface ####

class Interface_LocBoy(Funcoes_BD):
    def __init__(self, janela):
        self.Janela = janela
        self.Tela()
    
        #### Janela principal ####

    def Tela(self):
        self.Janela.title("LocBoy")
        self.Janela.configure(background="#9370DB")
        self.Janela.geometry("800x600")
        self.Janela.resizable(True, True)
        self.Janela.maxsize(width=1800, height=1000)
        self.Janela.minsize(width=600, height=400)
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
        self.Nome_Usuario = Entry(self.Frame_2)
        self.Nome_Usuario.place(relx=0.5, rely=0.08, relwidth=0.45, relheight=0.2)
        self.Texto_3 = Label(self.Frame_2, text="SENHA:",
                                             background="#FFFFFF", 
                                             foreground="#0000FF", 
                                             font="Arialblack 17")
        self.Texto_3.place(relx=0.04, rely=0.33, relwidth=0.42, relheight=0.2)
        self.Senha_Usuario = Entry(self.Frame_2)
        self.Senha_Usuario["show"]="*"
        self.Senha_Usuario.place(relx=0.5, rely=0.33, relwidth=0.45, relheight=0.2)
        self.Frame_3 = Frame(self.Janela, bg="#00FF00",
                            highlightbackground="#fff",
                            highlightthickness=2)
        self.Frame_3.place(relx=0.460, rely=0.3, relwidth=0.52, relheight=0.66)
        
        self.Botao_Entra = Button(self.Frame_2)
        self.Botao_Entra["text"] = "Entrar"
        self.Botao_Entra["font"] = ("Arial", "25", "bold")
        self.Botao_Entra["command"] = self.Login_Usuario
        self.Botao_Entra.place(relx=0.04, rely=0.6, relwidth=0.91, relheight=0.15)

        self.Botao_Cadastra = Button(self.Frame_2)
        self.Botao_Cadastra["text"] = "Cadastrar"
        self.Botao_Cadastra["font"] = ("Arial", "20", "bold")
        self.Botao_Cadastra["command"] = self.Janela_Tipo_Usuario
        self.Botao_Cadastra.place(relx=0.04, rely=0.78, relwidth=0.91, relheight=0.15)
        self.logo()

    def Login_Usuario(self):
        Nome_Usuario_Inf = self.Nome_Usuario.get();
        Senha_Usuario_Inf = self.Senha_Usuario.get();
        if (Nome_Usuario_Inf == "") and (Senha_Usuario_Inf == ""):
            print(Nome_Usuario_Inf)
            self.Janela_Usuario()
        else:
            print("usuário não cadastrado")
     
    def Janela_Usuario(self):
        self.V_Usuario = StringVar()
        self.V_Usuario.set(Lista_Usuario[0])
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
        self.Frame_2_Usuario = Frame(self.Janela_2, bg="#9370DB",
                            highlightbackground="#fff",
                            highlightthickness=4)
        self.Frame_2_Usuario.place(relx=0.02, rely=0.25, relwidth=0.96, relheight=0.70)
        self.Frame_3_Usuario = Frame(self.Janela_2, bg="#FFFFFF",
                            highlightbackground="#fff",
                            highlightthickness=2)
        self.Frame_3_Usuario.place(relx=0.78, rely=0.265, relwidth=0.185, relheight=0.25)
        self.Texto_2_Usuario = Label(self.Frame_2_Usuario, text="Usuário:")
        self.Texto_2_Usuario["background"]="#dde"
        self.Texto_2_Usuario["foreground"]="#000000" 
        self.Texto_2_Usuario["anchor"] = W
        self.Texto_2_Usuario.place(relx=0.025, rely=0.035, relwidth=0.1, relheight=0.065)
        self.Op_Usuario = OptionMenu(self.Frame_2_Usuario, self.V_Usuario, *Lista_Usuario)
        self.Op_Usuario["font"] = ("Calibri", "10")
        self.Op_Usuario["background"]="#FFFFFF" 
        self.Op_Usuario["foreground"]="#000"
        self.Op_Usuario.place(relx=0.135, rely=0.035, relwidth=0.35, relheight=0.065)
        self.Texto_3_Usuario = Label(self.Frame_2_Usuario, text="Nome:")
        self.Texto_3_Usuario["background"]="#dde"
        self.Texto_3_Usuario["foreground"]="#000000" 
        self.Texto_3_Usuario["anchor"] = W
        self.Texto_3_Usuario.place(relx=0.025, rely=0.125, relwidth=0.1, relheight=0.065)
        self.Nome_T_Usuario = Entry(self.Frame_2_Usuario)
        self.Nome_T_Usuario.place(relx=0.135, rely=0.125, relwidth=0.35, relheight=0.065)
        # self.Botao_Busca = Button(self.Frame_2_Usuario, text="Busca")
        # self.Botao_Busca["font"] = ("Calibri", "10")
        # self.Botao_Busca["background"]="#FFFFFF" 
        # self.Botao_Busca["foreground"]="#000"
       ##### inserir command aqui#####
        # self.Botao_Busca.place(relx=0.045, rely=0.212, relwidth=0.205, relheight=0.065)
        # self.Botao_Alterar = Button(self.Frame_2_Usuario, text="Alterar",)
        # self.Botao_Alterar["font"] = ("Calibri", "10")
        # self.Botao_Alterar["background"]="#FFFFFF" 
        # self.Botao_Alterar["foreground"]="#000"
       ##### inserir command aqui#####
        # self.Botao_Alterar.place(relx=0.265, rely=0.212, relwidth=0.205, relheight=0.065)
        self.grid()
    
    def grid(self):
        self.tv=ttk.Treeview(self.Frame_2_Usuario,column=('id','nome','numero','idade','senha','email','cpf','salario','plano','status'),show='headings')
        self.tv.heading('id',text='ID')
        self.tv.heading('nome',text='nome')
        self.tv.heading('cpf',text='cpf')
        self.tv.heading('numero',text='numero')
        self.tv.heading('idade',text='Idede')
        self.tv.heading('email',text='email')
        self.tv.heading('salario',text='salario')
        self.tv.heading('senha',text='senha')
        self.tv.heading('plano',text='plano')
        self.tv.heading('status',text='status')
        
        self.tv.column('id',width=3)
        self.tv.column('nome',width=25)
        self.tv.column('email',width=25)
        self.tv.column('numero',width=20)
        self.tv.column('idade',width=4)
        self.tv.column('senha',width=15)
        self.tv.column('salario',width=10)
        self.tv.column('plano',width=15)
        self.tv.column('cpf',width=20)
        self.tv.column('status',width=15)
        self.tv.place(relx=0.001, rely=0.5,relwidth=0.98 ,relheight=0.45)
    
        self.btn_deleta=Button(self.Frame_2_Usuario,text="criar tb",command=self.Criar_Tabela_BD)
        self.btn_dl_a=Button(self.Frame_2_Usuario,text="delete aluno",command=self.Exclui_BD_alu)
        self.btn_al_a=Button(self.Frame_2_Usuario,text="alterae aluno",command=self.alterar_BD_aluno)
        self.btn_al_f=Button(self.Frame_2_Usuario,text="alterae funcionario",command=self.alterar_BD_Func)
        self.btn_al_p=Button(self.Frame_2_Usuario,text="alterae profesor",command=self.alterar_BD_Prof)
        self.btn_al_c=Button(self.Frame_2_Usuario,text="alterae convidado",command=self.alterar_BD_Com)      
        self.btn_alu=Button(self.Frame_2_Usuario,text="cadastros",command=self.Atualizar_Listagem_BD_Alu)
       
        self.iemail=Label(self.Frame_2_Usuario,text="emial",)
        self.vemail=Entry(self.Frame_2_Usuario)
        self.ibfone=Label(self.Frame_2_Usuario,text="fone")
        self.vfone=Entry(self.Frame_2_Usuario)
        self.ibsalario=Label(self.Frame_2_Usuario,text="salario")
        self.vsalario=Entry(self.Frame_2_Usuario)
        self.ibidade=Label(self.Frame_2_Usuario,text="idade")
        self.vidade=Entry(self.Frame_2_Usuario)
        self.ibsenha=Label(self.Frame_2_Usuario,text="senha")
        self.vsenha=Entry(self.Frame_2_Usuario)
        self.ibcpf=Label(self.Frame_2_Usuario,text="cpf")
        self.vcpf=Entry(self.Frame_2_Usuario)
        self.ibplano=Label(self.Frame_2_Usuario,text="plano")
        self.vplano=Entry(self.Frame_2_Usuario)
        
        #       self.Texto_3_Usuario.place(relx=0.025, rely=0.125, relwidth=0.1, relheight=0.065)
        # self.Nome_T_Usuario = Entry(self.Frame_2_Usuario)
        # self.Nome_T_Usuario.place(relx=0.135, rely=0.125, relwidth=0.35, relheight=0.065)
        self.btn_deleta.place(relx=0.45, rely=0.535,relwidth=0.09 ,relheight=0.06)
        self.iemail.place(relx=0.025, rely=0.235,relwidth=0.09 ,relheight=0.06)
        self.vemail.place(relx=0.115,rely=0.235,relwidth=0.25,relheight=0.06)
        self.ibfone.place(relx=0.025, rely=0.300,relwidth=0.09,relheight=0.06)
        self.vfone.place(relx=0.115, rely=0.300,relwidth=0.25,relheight=0.06)
        self.ibidade.place(relx=0.37, rely=0.3,relwidth=0.09 ,relheight=0.06)
        self.vidade.place(relx=0.45, rely=0.3,relwidth=0.25 ,relheight=0.06)
        self.ibsenha.place(relx=0.025, rely=0.37,relwidth= 0.09,relheight=0.06)
        self.vsenha.place(relx=0.110, rely=0.37,relwidth=0.25,relheight=0.06)
        self.ibsalario.place(relx=0.37, rely=0.37,relwidth=0.09 ,relheight=0.06)
        self.vsalario.place(relx=0.45, rely=0.37,relwidth=0.25 ,relheight=0.06)
        self.ibcpf.place(relx=0.705, rely=0.4,relwidth=0.09,relheight=0.06)
        self.vcpf.place(relx=0.77, rely=0.4,relwidth=0.23,relheight=0.06)
        self.ibplano.place(relx=0.37, rely=0.235,relwidth=0.09,relheight=0.06)
        self.vplano.place(relx=0.45, rely=0.235,relwidth=0.25,relheight=0.06)
        
        self.btn_dl_a.place(relx=0.50, rely=0.05,relwidth=0.14,relheight=0.04)
       
        self.btn_alu.place(relx=0.65, rely=0.05,relwidth=0.14,relheight=0.04)
        self.btn_al_a.place(relx=0.65, rely=0.15,relwidth=0.14,relheight=0.04)
        self.btn_al_c.place(relx=0.50, rely=0.15,relwidth=0.14,relheight=0.04)
        self.btn_al_p.place(relx=0.50, rely=0.10,relwidth=0.14,relheight=0.04)
        self.btn_al_f.place(relx=0.65, rely=0.10,relwidth=0.14,relheight=0.04)
        
        # self.imag=PhotoImage(file="cpf/logo.png.png")
        # self.label_imagen=Label(Janela,image=self.imag)
        # self.label_imagen(relx=0.65, rely=0.10,relwidth=0.14,relheight=0.04)
        
        self.scrolllistagem=Scrollbar(self.Frame_2_Usuario,orient='vertical')  
        self.tv.configure(yscroll=self.scrolllistagem.set)
        self.scrolllistagem.place(relx=0.98,rely=0.50,relheight=0.45)
        self.tv.bind("<Double-1>",self.clique_duplo)
   
    def logo(self): 
        self.imag=PhotoImage(file="cpf/logo.png.png")
        self.label_imagen=Label(self.Frame_3,image=self.imag)
        self.label_imagen.place(relx=0.0, rely=0.0, relwidth=1.7, relheight=1.5)
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

    def Janela_Cadastro_Funcionário(self):
        self.V_Mat = 1
        self.V_Id = 0
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
        self.Frame_7 = Frame(self.Janela_4, bg="#00FF00",
                            highlightbackground="#fff",
                            highlightthickness=4)
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
        self.Nome_Fun = Entry(self.Frame_8)
        self.Nome_Fun.place(relx=0.135, rely=0.025, relwidth=0.35, relheight=0.065)
        self.Texto_9 = Label(self.Frame_8, text="Cpf:")
        self.Texto_9["background"]="#dde"
        self.Texto_9["foreground"]="#00f" 
        self.Texto_9["anchor"] = W
        self.Texto_9.place(relx=0.025, rely=0.105, relwidth=0.1, relheight=0.065)
        self.Cpf_Fun = Entry(self.Frame_8)
        self.Cpf_Fun.place(relx=0.135, rely=0.105, relwidth=0.35, relheight=0.065)
        self.Texto_10 = Label(self.Frame_8, text="Email:")
        self.Texto_10["background"]="#dde"
        self.Texto_10["foreground"]="#00f" 
        self.Texto_10["anchor"] = W
        self.Texto_10.place(relx=0.025, rely=0.185, relwidth=0.1, relheight=0.065)
        self.Email_Fun = Entry(self.Frame_8)
        self.Email_Fun.place(relx=0.135, rely=0.185, relwidth=0.35, relheight=0.065)
        self.Texto_11 = Label(self.Frame_8, text="Tel:")
        self.Texto_11["background"]="#dde"
        self.Texto_11["foreground"]="#00f" 
        self.Texto_11["anchor"] = W
        self.Texto_11.place(relx=0.025, rely=0.268, relwidth=0.1, relheight=0.065)
        self.Tel_Fun = Entry(self.Frame_8)
        self.Tel_Fun.place(relx=0.135, rely=0.268, relwidth=0.35, relheight=0.065)
        self.Texto_12 = Label(self.Frame_8, text="Senha:")
        self.Texto_12["background"]="#dde"
        self.Texto_12["foreground"]="#00f" 
        self.Texto_12["anchor"] = W
        self.Texto_12.place(relx=0.025, rely=0.350, relwidth=0.1, relheight=0.065)
        self.Senha_Fun = Entry(self.Frame_8)
        self.Senha_Fun.place(relx=0.135, rely=0.350, relwidth=0.35, relheight=0.065)
        self.Texto_13 = Label(self.Frame_8, text="Salário:")
        self.Texto_13["background"]="#dde"
        self.Texto_13["foreground"]="#00f" 
        self.Texto_13["anchor"] = W
        self.Texto_13.place(relx=0.025, rely=0.430, relwidth=0.1, relheight=0.065)
        self.Salario_Fun = Entry(self.Frame_8)
        self.Salario_Fun.place(relx=0.135, rely=0.430, relwidth=0.35, relheight=0.065)
        self.Botao_7 = Button(self.Frame_8, text="Salvar")
        self.Botao_7["font"] = ("Calibri", "10")
        self.Botao_7["background"]="#FFFFFF" 
        self.Botao_7["foreground"]="#000"
        self.Botao_7["command"] = self.Pegar_Dados_Fun
        self.Botao_7.place(relx=0.135, rely=0.512, relwidth=0.35, relheight=0.065)
        self.Texto_14 = Label(self.Frame_8, text="", background= "#fff", foreground="#000")
        self.Texto_14.place(relx=0.50, rely=0.025, relwidth=0.28, relheight=0.47)
        self.Botao_Foto_Fun = Button(self.Frame_8, text="Foto",)
        self.Botao_Foto_Fun["font"] = ("Calibri", "10")
        self.Botao_Foto_Fun["background"]="#FFFFFF" 
        self.Botao_Foto_Fun["foreground"]="#000"
        #### epaço para command pegar foto ####
        self.Botao_Foto_Fun.place(relx=0.802, rely=0.362, relwidth=0.176, relheight=0.065)
      
    def Pegar_Dados_Fun(self):
        Nome_Fun_Inf = self.Nome_Fun.get();
        Cpf_Fun_Inf = self.Cpf_Fun.get();
        Email_Fun_Inf = self.Email_Fun.get();
        Tel_Fun_Inf = self.Tel_Fun.get();
        Senha_Fun_Inf = self.Senha_Fun.get();
        Salario_Fun_Inf =float(self.Salario_Fun.get());
        print(f"Nome: {Nome_Fun_Inf}");
        print(f"CPF: {Cpf_Fun_Inf}");
        print(f"Email: {Email_Fun_Inf}");
        print(f"Tel: {Tel_Fun_Inf}");
        print(f"Senha: {Senha_Fun_Inf}");
        print(f"Salário: {Salario_Fun_Inf}");
        self.validacao(Cpf_Fun_Inf)
        if Salario_Fun_Inf > 0 and self.validacao(Cpf_Fun_Inf)==True:
            self.Cadastrar_BD_func()
            self.Texto_14["text"] = (f"Nome: {Nome_Fun_Inf}\nCpf: {Cpf_Fun_Inf}\nEmail:\n{Email_Fun_Inf}\n{Tel_Fun_Inf}\n{Salario_Fun_Inf}\n\nUSUÁRIO SALVO COM SUCESSO!")
            
        else:
            self.Texto_14["text"] = (f"Digite um valor valido para salário ou CPF! ")
           
    def validacao(self,cpf):
        cpf3=cpf
        str(cpf3)
        print(f"cpf3: {cpf3}")
        validacpf(cpf3)
        print(validacpf(cpf3))
        cpf=validacpf(cpf3)
        if cpf.valida():
            print("cpf valido5")
            return True
        else:
            print("cpf invalio5")
            print(validacpf(cpf3))
            return False
        
    def Janela_Cadastro_Aluno(self):
        self.V_Plano = StringVar()
        self.V_Plano.set(Lista_Plano[0])
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
        self.Frame_10 = Frame(self.Janela_5, bg="#00FF00",
                            highlightbackground="#fff",
                            highlightthickness=4)
        self.Frame_10.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.12)
        self.Texto_15 = Label(self.Frame_10, text="Academia LocBoy",
                                             background="#00FF00", 
                                             foreground="#0000FF", 
                                             font="Gotham 30")
        self.Texto_15.place(relx=0.02, rely=0.002, relwidth=0.96, relheight=1)
        self.Frame_11 = Frame(self.Janela_5, bg="#00FF00",
                            highlightbackground="#fff",
                            highlightthickness=2)
        self.Frame_11.place(relx=0.02, rely=0.185, relwidth=0.96, relheight=0.77)
        self.Frame_12 = Frame(self.Janela_5, bg="#FFFFFF",
                            highlightbackground="#fff",
                            highlightthickness=2)
        self.Frame_12.place(relx=0.78, rely=0.205, relwidth=0.185, relheight=0.25)
        self.Texto_16 = Label(self.Frame_11, text="Nome:")
        self.Texto_16["background"]="#dde"
        self.Texto_16["foreground"]="#00f" 
        self.Texto_16["anchor"] = W
        self.Texto_16.place(relx=0.025, rely=0.025, relwidth=0.1, relheight=0.065)
        self.Nome_Alu = Entry(self.Frame_11)
        self.Nome_Alu.place(relx=0.135, rely=0.025, relwidth=0.35, relheight=0.065)
        self.Texto_17 = Label(self.Frame_11, text="Cpf:")
        self.Texto_17["background"]="#dde"
        self.Texto_17["foreground"]="#00f" 
        self.Texto_17["anchor"] = W
        self.Texto_17.place(relx=0.025, rely=0.105, relwidth=0.1, relheight=0.065)
        self.Cpf_Alu = Entry(self.Frame_11)
        self.Cpf_Alu.place(relx=0.135, rely=0.105, relwidth=0.35, relheight=0.065)
        self.Texto_18 = Label(self.Frame_11, text="Email:")
        self.Texto_18["background"]="#dde"
        self.Texto_18["foreground"]="#00f" 
        self.Texto_18["anchor"] = W
        self.Texto_18.place(relx=0.025, rely=0.185, relwidth=0.1, relheight=0.065)
        self.Email_Alu = Entry(self.Frame_11)
        self.Email_Alu.place(relx=0.135, rely=0.185, relwidth=0.35, relheight=0.065)
        self.Texto_19 = Label(self.Frame_11, text="Tel:")
        self.Texto_19["background"]="#dde"
        self.Texto_19["foreground"]="#00f" 
        self.Texto_19["anchor"] = W
        self.Texto_19.place(relx=0.025, rely=0.268, relwidth=0.1, relheight=0.065)
        self.Tel_Alu = Entry(self.Frame_11)
        self.Tel_Alu.place(relx=0.135, rely=0.268, relwidth=0.35, relheight=0.065)
        self.Texto_20 = Label(self.Frame_11, text="Idade:")
        self.Texto_20["background"]="#dde"
        self.Texto_20["foreground"]="#00f" 
        self.Texto_20["anchor"] = W
        self.Texto_20.place(relx=0.025, rely=0.350, relwidth=0.1, relheight=0.065)
        self.Idade_Alu = Entry(self.Frame_11)
        self.Idade_Alu.place(relx=0.135, rely=0.350, relwidth=0.35, relheight=0.065)
        self.Texto_21 = Label(self.Frame_11, text="Senha:")
        self.Texto_21["background"]="#dde"
        self.Texto_21["foreground"]="#00f" 
        self.Texto_21["anchor"] = W
        self.Texto_21.place(relx=0.025, rely=0.509, relwidth=0.1, relheight=0.065)
        self.Senha_Alu = Entry(self.Frame_11)
        self.Senha_Alu.place(relx=0.135, rely=0.509, relwidth=0.35, relheight=0.065)
        self.Texto_22 = Label(self.Frame_11, text="Plano:")
        self.Texto_22["background"]="#dde"
        self.Texto_22["foreground"]="#00f" 
        self.Texto_22["anchor"] = W
        self.Texto_22.place(relx=0.025, rely=0.430, relwidth=0.1, relheight=0.065)
        self.Op_Plano = OptionMenu(self.Frame_11, self.V_Plano, *Lista_Plano)
        self.Op_Plano["font"] = ("Calibri", "10")
        self.Op_Plano["background"]="#FFFFFF" 
        self.Op_Plano["foreground"]="#000"
        self.Op_Plano.place(relx=0.135, rely=0.430, relwidth=0.35, relheight=0.065)
        self.Botao_8 = Button(self.Frame_11, text="Salvar")
        self.Botao_8["font"] = ("Calibri", "10")
        self.Botao_8["background"]="#FFFFFF" 
        self.Botao_8["foreground"]="#000"
        self.Botao_8["command"] = self.Pegar_Dados_Alunos
        self.Botao_8.place(relx=0.135, rely=0.591, relwidth=0.35, relheight=0.065)
        self.Texto_23 = Label(self.Frame_11, text="", background= "#fff", foreground="#000")
        self.Texto_23.place(relx=0.50, rely=0.025, relwidth=0.28, relheight=0.56)
        self.Botao_Foto_Alu = Button(self.Frame_11, text="Foto")
        self.Botao_Foto_Alu["font"] = ("Calibri", "10")
        self.Botao_Foto_Alu["background"]="#FFFFFF" 
        self.Botao_Foto_Alu["foreground"]="#000"
        #### epaço para command pegar foto ####
        self.Botao_Foto_Alu.place(relx=0.802, rely=0.362, relwidth=0.176, relheight=0.065)

    def Pegar_Dados_Alunos(self):
        Nome_Alu_Inf = self.Nome_Alu.get();
        Cpf_Alu_Inf = self.Cpf_Alu.get();
        Email_Alu_Inf = self.Email_Alu.get();
        Tel_Alu_Inf = self.Tel_Alu.get();
        Idade_Alu_Inf = int(self.Idade_Alu.get());
        Senha_Alu_Inf = self.Senha_Alu.get();
        Inf_Plano = self.V_Plano.get();
        self.validacao(Cpf_Alu_Inf)
        print(f"Nome: {Nome_Alu_Inf}");
        print(f"CPF: {Cpf_Alu_Inf}");
        print(f"Email: {Email_Alu_Inf}");
        print(f"Tel: {Tel_Alu_Inf}");
        print(f"Idade: {Idade_Alu_Inf}");
        print(f"Senha: {Senha_Alu_Inf}");
        print(f"Plano: {Inf_Plano}");
        if (Idade_Alu_Inf > 1 and Idade_Alu_Inf < 100) and (Inf_Plano == "Plano Básico")and (self.validacao(Cpf_Alu_Inf)==True):
            self.plano_Alu="Plano Básico"
            self.Cadastrar_BD_alu()
            self.Texto_23["text"] = (f"Nome: {Nome_Alu_Inf}\nCpf: {Cpf_Alu_Inf}\nEmail: {Email_Alu_Inf}\nTel: {Tel_Alu_Inf}\nIdade: {Idade_Alu_Inf}\nMensalidade: R$ 70,00\n\nUSUÁRIO SALVO COM SUCESSO!")
            self.Nome_Alu.delete(0,END)
            self.Cpf_Alu.delete(0,END)
            self.Email_Alu.delete(0,END)
            self.Tel_Alu.delete(0,END)
            self.Idade_Alu.delete(0,END)
            self.Senha_Alu.delete(0,END)

        elif (Idade_Alu_Inf > 1 and Idade_Alu_Inf < 100) and (Inf_Plano == "Plano Médio")  and (self.validacao(Cpf_Alu_Inf)==True):
            self.plano_Alu="Plano Médio"
            self.Cadastrar_BD_alu()
            self.Texto_23["text"] = (f"Nome: {Nome_Alu_Inf}\nCpf: {Cpf_Alu_Inf}\nEmail: {Email_Alu_Inf}\nTel: {Tel_Alu_Inf}\nIdade: {Idade_Alu_Inf}\nMensalidade: R$ 120,00\n\nUSUÁRIO SALVO COM SUCESSO!")
            self.Nome_Alu.delete(0,END)
            self.Cpf_Alu.delete(0,END)
            self.Email_Alu.delete(0,END)
            self.Tel_Alu.delete(0,END)
            self.Idade_Alu.delete(0,END)
            self.Senha_Alu.delete(0,END)
        elif (Idade_Alu_Inf > 1 and Idade_Alu_Inf < 100) and (Inf_Plano == "Plano Completo")and self.validacao(Cpf_Alu_Inf)==True:
            self.plano_Alu="Plano Completo"
            self.Cadastrar_BD_alu()
            self.Texto_23["text"] = (f"Nome: {Nome_Alu_Inf}\nCpf: {Cpf_Alu_Inf}\nEmail: {Email_Alu_Inf}\nTel: {Tel_Alu_Inf}\nIdade: {Idade_Alu_Inf}\nMensalidade: R$ 150,00\n\nUSUÁRIO SALVO COM SUCESSO!")
            self.Nome_Alu.delete(0,END)
            self.Cpf_Alu.delete(0,END)
            self.Email_Alu.delete(0,END)
            self.Tel_Alu.delete(0,END)
            self.Idade_Alu.delete(0,END)
            self.Senha_Alu.delete(0,END)
        else:
            self.Texto_23["text"] = ("Digite um valor válido para idade ou CPF!")

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
        self.Frame_Prof_1 = Frame(self.Janela_6, bg="#00FF00",
                            highlightbackground="#fff",
                            highlightthickness=4)
        self.Frame_Prof_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.12)
        self.Texto_Prof_1 = Label(self.Frame_Prof_1, text="Academia LocBoy",
                                             background="#00FF00", 
                                             foreground="#0000FF", 
                                             font="Gotham 30")
        self.Texto_Prof_1.place(relx=0.02, rely=0.002, relwidth=0.96, relheight=1)
        self.Frame_Prof_2 = Frame(self.Janela_6, bg="#00FF00",
                            highlightbackground="#fff",
                            highlightthickness=2)
        self.Frame_Prof_2.place(relx=0.02, rely=0.185, relwidth=0.96, relheight=0.77)
        self.Frame_Prof_3 = Frame(self.Janela_6, bg="#FFFFFF",
                            highlightbackground="#fff",
                            highlightthickness=2)
        self.Frame_Prof_3.place(relx=0.78, rely=0.205, relwidth=0.185, relheight=0.25)
        self.Texto_Prof_2 = Label(self.Frame_Prof_2, text="Nome:")
        self.Texto_Prof_2["background"]="#dde"
        self.Texto_Prof_2["foreground"]="#00f" 
        self.Texto_Prof_2["anchor"] = W
        self.Texto_Prof_2.place(relx=0.025, rely=0.025, relwidth=0.1, relheight=0.065)
        self.Nome_Prof = Entry(self.Frame_Prof_2)
        self.Nome_Prof.place(relx=0.135, rely=0.025, relwidth=0.35, relheight=0.065)
        self.Texto_Prof_3 = Label(self.Frame_Prof_2, text="Cpf:")
        self.Texto_Prof_3["background"]="#dde"
        self.Texto_Prof_3["foreground"]="#00f" 
        self.Texto_Prof_3["anchor"] = W
        self.Texto_Prof_3.place(relx=0.025, rely=0.105, relwidth=0.1, relheight=0.065)
        self.Cpf_Prof = Entry(self.Frame_Prof_2)
        self.Cpf_Prof.place(relx=0.135, rely=0.105, relwidth=0.35, relheight=0.065)
        self.Texto_Prof_4 = Label(self.Frame_Prof_2, text="Email:")
        self.Texto_Prof_4["background"]="#dde"
        self.Texto_Prof_4["foreground"]="#00f" 
        self.Texto_Prof_4["anchor"] = W
        self.Texto_Prof_4.place(relx=0.025, rely=0.185, relwidth=0.1, relheight=0.065)
        self.Email_Prof = Entry(self.Frame_Prof_2)
        self.Email_Prof.place(relx=0.135, rely=0.185, relwidth=0.35, relheight=0.065)
        self.Texto_Prof_5 = Label(self.Frame_Prof_2, text="Tel:")
        self.Texto_Prof_5["background"]="#dde"
        self.Texto_Prof_5["foreground"]="#00f" 
        self.Texto_Prof_5["anchor"] = W
        self.Texto_Prof_5.place(relx=0.025, rely=0.268, relwidth=0.1, relheight=0.065)
        self.Tel_Prof = Entry(self.Frame_Prof_2)
        self.Tel_Prof.place(relx=0.135, rely=0.268, relwidth=0.35, relheight=0.065)
        self.Texto_Prof_6 = Label(self.Frame_Prof_2, text="Senha:")
        self.Texto_Prof_6["background"]="#dde"
        self.Texto_Prof_6["foreground"]="#00f" 
        self.Texto_Prof_6["anchor"] = W
        self.Texto_Prof_6.place(relx=0.025, rely=0.350, relwidth=0.1, relheight=0.065)
        self.Senha_Prof = Entry(self.Frame_Prof_2)
        self.Senha_Prof.place(relx=0.135, rely=0.350, relwidth=0.35, relheight=0.065)
        self.Texto_Prof_7 = Label(self.Frame_Prof_2, text="Salário:")
        self.Texto_Prof_7["background"]="#dde"
        self.Texto_Prof_7["foreground"]="#00f" 
        self.Texto_Prof_7["anchor"] = W
        self.Texto_Prof_7.place(relx=0.025, rely=0.430, relwidth=0.1, relheight=0.065)
        self.Salario_Prof = Entry(self.Frame_Prof_2)
        self.Salario_Prof.place(relx=0.135, rely=0.430, relwidth=0.35, relheight=0.065)
        self.Botao_7 = Button(self.Frame_Prof_2, text="Salvar")
        self.Botao_7["font"] = ("Calibri", "10")
        self.Botao_7["background"]="#FFFFFF" 
        self.Botao_7["foreground"]="#000"
        self.Botao_7["command"] = self.Pegar_Dados_Prof
        self.Botao_7.place(relx=0.135, rely=0.512, relwidth=0.35, relheight=0.065)
        self.Texto_Prof_8 = Label(self.Frame_Prof_2, text="", background= "#fff", foreground="#000")
        self.Texto_Prof_8.place(relx=0.50, rely=0.025, relwidth=0.28, relheight=0.47)
        self.Botao_Foto_Prof = Button(self.Frame_Prof_2, text="Foto")
        self.Botao_Foto_Prof["font"] = ("Calibri", "10")
        self.Botao_Foto_Prof["background"]="#FFFFFF" 
        self.Botao_Foto_Prof["foreground"]="#000"
        #### epaço para command pegar foto ####
        self.Botao_Foto_Prof.place(relx=0.802, rely=0.362, relwidth=0.176, relheight=0.065)

    def Pegar_Dados_Prof(self):
        Nome_Prof_Inf = self.Nome_Prof.get();
        Cpf_Prof_Inf = self.Cpf_Prof.get();
        Email_Prof_Inf = self.Email_Prof.get();
        Tel_Prof_Inf = self.Tel_Prof.get();
        Senha_Prof_Inf = self.Senha_Prof.get();
        Salario_Prof_Inf =float(self.Salario_Prof.get());
        print(f"Nome: {Nome_Prof_Inf}");
        print(f"CPF: {Cpf_Prof_Inf}");
        print(f"Email: {Email_Prof_Inf}");
        print(f"Tel: {Tel_Prof_Inf}");
        print(f"Senha: {Senha_Prof_Inf}");
        print(f"Salário: {Salario_Prof_Inf}");
        if (Salario_Prof_Inf > 0)and self.validacao(Cpf_Prof_Inf)==True:
            self.Cadastrar_BD_Prof()
            self.Texto_Prof_8["text"] = (f"Nome: {Nome_Prof_Inf}\nCpf: {Cpf_Prof_Inf}\nEmail:{Email_Prof_Inf}\nTel:{Tel_Prof_Inf}\nSalário\n{Salario_Prof_Inf}\n\nUSUÁRIO SALVO COM SUCESSO!")
        else:
            self.Texto_Prof_8["text"] = (f"Digite um valor valido para salário ou cpf!")

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
        self.Frame_Con_1 = Frame(self.Janela_7, bg="#00FF00",
                            highlightbackground="#fff",
                            highlightthickness=4)
        self.Frame_Con_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.12)
        self.Texto_Con_1 = Label(self.Frame_Con_1, text="Academia LocBoy",
                                             background="#00FF00", 
                                             foreground="#0000FF", 
                                             font="Gotham 30")
        self.Texto_Con_1.place(relx=0.02, rely=0.002, relwidth=0.96, relheight=1)
        self.Frame_Con_2 = Frame(self.Janela_7, bg="#00FF00",
                            highlightbackground="#fff",
                            highlightthickness=2)
        self.Frame_Con_2.place(relx=0.02, rely=0.185, relwidth=0.96, relheight=0.77)
        self.Texto_Con_2 = Label(self.Frame_Con_2, text="Nome:")
        self.Texto_Con_2["background"]="#dde"
        self.Texto_Con_2["foreground"]="#00f" 
        self.Texto_Con_2["anchor"] = W
        self.Texto_Con_2.place(relx=0.025, rely=0.025, relwidth=0.1, relheight=0.065)
        self.Nome_Con = Entry(self.Frame_Con_2)
        self.Nome_Con.place(relx=0.135, rely=0.025, relwidth=0.35, relheight=0.065)
        self.Texto_Con_5 = Label(self.Frame_Con_2, text="Tel:")
        self.Texto_Con_5["background"]="#dde"
        self.Texto_Con_5["foreground"]="#00f" 
        self.Texto_Con_5["anchor"] = W
        self.Texto_Con_5.place(relx=0.025, rely=0.105, relwidth=0.1, relheight=0.065)
        self.Tel_Con = Entry(self.Frame_Con_2)
        self.Tel_Con.place(relx=0.135, rely=0.105, relwidth=0.35, relheight=0.065)
        self.Botao_Salva_Con = Button(self.Frame_Con_2, text="Salvar")
        self.Botao_Salva_Con["font"] = ("Calibri", "10")
        self.Botao_Salva_Con["background"]="#FFFFFF" 
        self.Botao_Salva_Con["foreground"]="#000"
        self.Botao_Salva_Con["command"] = self.Pegar_Con
        self.Botao_Salva_Con.place(relx=0.135, rely=0.185, relwidth=0.35, relheight=0.065)

    def Pegar_Con(self):
        Inf_Nome_Con = self.Nome_Con.get();
        Inf_Tel_Con = self.Tel_Con.get();
        self.Cadastrar_BD_Com()
        print(Inf_Nome_Con)
        print(Inf_Tel_Con)

       
Janela = Tk()
Interface_LocBoy(Janela)
Janela.mainloop()