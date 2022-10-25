
import sqlite3
from sqlite3 import Error
from tkinter import END, filedialog
from tkinter.ttk import Treeview
import os
from tkinter import messagebox
from tkinter import *
from tkinter import ttk


if os.name=="nt":
    os.system("cls");

class Pessoa:
    def __init__(self,id,nome,numero,idade,sexo,matrícula,cpf):
        self.id=id
        print(f"id={self.id}")
        self.nome=nome
        print(f"nome={self.nome}")
        self.numero=numero
        print(f"numero={self.numero}")
        self.idade=idade
        print(f"idade={self.idade}")
        self.sexo=sexo
        print(f"sexo={self.sexo}")
        self.matricula=matrícula
        print(f"matricula={self.matricula}")
        self.cpf=cpf
        print(f"cpf={self.cpf}")
               
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

    def alterar_BD(self):
        self.Pega_dados()  
        self.Conexao_BD()
        Comando = f"""UPDATE aluno SET nome='{self.Liv.nome}',
        idade={self.Liv.idade},matricula={self.Liv.matricula},
        id={self.Liv.id},sexo={self.Liv.sexo},cpf={self.Liv.cpf},
        numero={self.Liv.telefone} where id ='{self.Liv.id}'"""
        self.cursor.execute(Comando)
        self.conex_banco.commit()
        print("elemento alterado com sucesso")
        self.desconectaBD()
        self.Limpar_Campos()

    def Exclui_BD(self):
        self.Pega_dados()
        self.Conexao_BD()
        Comando= f"""DELETE FROM Aluno WHERE id='{self.Liv.id}'  """
        self.cursor.execute(Comando)
        self.conex_banco.commit()
        print("Elemento excluido com Sucesso!")
        self.desconectaBD()
        self.Limpar_Campos()

    def Atualizar_Listagem_BD(self):
        self.tv.delete(*self.tv.get_children())
        self.Conexao_BD()
        Lista = self.cursor.execute("""SELECT ID, nome,numero, idade, sexo,matricula, cpf FROM aluno ORDER BY ID ASC;""")
        for i in Lista:
            self.tv.insert("",END,values=i)
        self.desconectaBD()
        
    def Cadastrar_BD(self):
        self.Pega_dados()
        self.Conexao_BD() 
        self.cursor.execute(f"""INSERT INTO Aluno(id,nome,numero,idade,sexo,matricula,cpf) VALUES 
        ({self.Liv.id},'{self.Liv.nome}',{self.Liv.numero},{self.Liv.idade},
        '{self.Liv.sexo}',{self.Liv.matricula},{self.Liv.cpf}) """)
        self.conex_banco.commit();
        self.desconectaBD()
        self.Limpar_Campos()

    def Pega_dados(self): 
        self.Liv = Pessoa(id=self.vid.get(),nome=self.vnome.get(),cpf=self.vcpf.get(),numero= self.vfone.get(),idade= self.vidade.get(),sexo=self.vsexo.get(),matrícula=self.vmatricula.get())
        print (self.vid.get(),self.vnome.get(),self.vfone.get(),self.vidade.get(),self.vsexo.get(),self.vmatricula.get(),self.vcpf.get())
    def Criar_Tabela_BD(self):
        try: 
            self.Conexao_BD()
            Comando="""CREATE TABLE IF NOT EXISTS aluno(ID INTEGER PRIMARY KEY,nome VARCHAR (100),
            matricula integer not null,
            CPF VARCHAR(30) NOT NULL,
            numero integer ,
            idade intege,
            sexo text);"""
            self.cursor.execute(Comando)
            self.conex_banco.commit()
            print("Tabela Criada com Sucesso!") 
            self.desconectaBD() 
        except Error as erros:
            print("Criação da TABELA FALHOU: ", erros)
    def Limpar_Campos (self):
        self.vid.delete(0,END,)
        self.vfone.delete(0,END,)
        self.vnome.delete(0,END,)
        self.vidade.delete(0,END,)
        self.vmatricula.delete(0,END,)
        self.vcpf.delete(0,END,)
        self.vsexo.delete(0,END,)

    def clique_duplo(self, event):
        self.Limpar_Campos() 
        self.tv.selection()
        for m in self.tv.selection():
            id,nome,numero,idade, sexo, matricula,cpf=self.tv.item(m,'values')
            self.vid.insert(END,id)
            self.vnome.insert(END,nome); 
            self.vidade.insert (END,idade);
            self.vmatricula.insert(END,matricula);
            self.vsexo.insert(END,sexo);
            self.vfone.insert(END,numero);
            self.vcpf.insert(END,cpf);


# def inserir():
#     if vid.get()=="" or vnome.get()=="" or vfone.get()=="":
#         messagebox.showinfo(title="ERRO",message="digiti todos os dados")
#         return
#     tv.insert("","end",values=(vid.get(),vnome.get(),vfone.get(),vidade.get(),vsexo.get(),))
#     vid.focus()

class Nova_Tela(Funcoes_BD):
    def __init__(self,janela):
        self.Janela = janela
        self.Tela() #chamada da Função
        self.grid()
    def Tela(self):#tela principal
        self.Janela.title("Aula 03/06/2022")
        self.Janela.configure(background="#4e5263")
        self.Janela.geometry("1500x1800")
        self.Janela.resizable(True, True)
        self.Janela.maxsize(width=1000, height=800)
        self.Janela.minsize(width=600, height=400)    
    
    def grid(self):
        # v=['2','kain','2222','20','2','sexo'],['1','murilo','33333','30','2','masc'],['3','lau','1111','40','3','femi']
        
        self.tv=ttk.Treeview(Janela,columns=('id','nome','numero','idade','sexo','matricula','cpf'),show='headings')
        self.tv.column('id',width=50)
        self.tv.column('nome',width=120)
        self.tv.column('matricula',width=100)
        self.tv.column('numero',width=100)
        self.tv.column('idade',width=100)
        self.tv.column('sexo',width=100)
        self.tv.column('cpf',width=200)
        self.tv.heading('id',text='ID')
        self.tv.heading('cpf',text='cpf')
        self.tv.heading('nome',text='nome')
        self.tv.heading('numero',text='numero')
        self.tv.heading('matricula',text='matricula')
        self.tv.heading('idade',text='Idede')
        self.tv.heading('sexo',text='sexo')
        self.tv.place(relx=0.05, rely=0.1,relwidth=0.7 ,relheight=0.4)
        print("o i") 
        self.btn_inserir=Button(Janela,text="cadstras",command=self.Cadastrar_BD )
        self.btn_deleta=Button(Janela,text="criar tb",command=self.Criar_Tabela_BD)
        self.btn_obter=Button(Janela,text="delete",command=self.Exclui_BD)
        self.btn_al=Button(Janela,text="alterae",command=self.alterar_BD)
        self.btn_at=Button(Janela,text="atualizar",command=self.Atualizar_Listagem_BD)
        
        self.ibid=Label(Janela,text="id",)
        self.vid=Entry(Janela)
        self.ibnome=Label(Janela,text="nome",)
        self.vnome=Entry(Janela)
        self.ibfone=Label(Janela,text="fone")
        self.vfone=Entry(Janela)
        self.ibmatricula=Label(Janela,text="matricula",anchor=W)
        self.vmatricula=Entry(Janela)
        self.ibidade=Label(Janela,text="idade",anchor=W)
        self.vidade=Entry(Janela)
        self.ibsexo=Label(Janela,text="sexo",anchor=W)
        self.vsexo=Entry(Janela)
        self.ibcpf=Label(Janela,text="cpf",anchor=W)
        self.vcpf=Entry(Janela)
        self.ibid.place(relx=0.0, rely=0.6,relwidth=0.05 ,relheight=0.03)
        self.vid.place(relx=0.045,rely=0.6,relwidth=0.05,relheight=0.03)
        self.ibnome.place(relx=0.08, rely=0.6,relwidth=0.05 ,relheight=0.03)
        self.vnome.place(relx=0.12, rely=0.6,relwidth=0.05 ,relheight=0.03)
        self.ibfone.place(relx=0.16, rely=0.6,relwidth=0.05,relheight=0.03)
        self.vfone.place(relx=0.20, rely=0.6,relwidth=0.05 ,relheight=0.03)
        self.ibidade.place(relx=0.32, rely=0.6,relwidth=0.05 ,relheight=0.03)
        self.vidade.place(relx=0.36, rely=0.6,relwidth=0.05 ,relheight=0.03)
        self.ibsexo.place(relx=0.40, rely=0.6,relwidth= 0.05,relheight=0.03)
        self.vsexo.place(relx=0.44, rely=0.6,relwidth=0.05,relheight=0.03)
        self.ibmatricula.place(relx=0.48, rely=0.6,relwidth=0.05 ,relheight=0.03)
        self.vmatricula.place(relx=0.52, rely=0.6,relwidth=0.05 ,relheight=0.03)
        self.ibcpf.place(relx=0.56, rely=0.6,relwidth=0.05,relheight=0.03)
        self.vcpf.place(relx=0.60, rely=0.7,relwidth=0.05,relheight=0.03)

        self.btn_inserir.place(relx=0.04, rely=0.01,relwidth=0.12,relheight=0.03)
        self.btn_deleta.place(relx=0.16, rely=0.01,relwidth=0.12,relheight=0.03)
        self.btn_obter.place(relx=0.26, rely=0.01,relwidth=0.12,relheight=0.03)
        self.btn_al.place(relx=0.36, rely=0.01,relwidth=0.12,relheight=0.03)
        self.btn_at.place(relx=0.46, rely=0.01,relwidth=0.12,relheight=0.03)
        
        self.scrolllistagem=Scrollbar(self.Janela,orient='vertical')  
        self.tv.configure(yscroll=self.scrolllistagem.set)
        self.scrolllistagem.place(relx=0.77,rely=0.060,relheight=0.58)
        self.tv.bind("<Double-1>",self.clique_duplo)


Janela = Tk()
Nova_Tela(Janela)
Janela.mainloop()
