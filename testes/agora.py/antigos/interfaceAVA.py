import os
from unittest import result
import banco1
from tkinter import *
from tkinter import ttk
import re
if os.name == "nt":
    os.system("cls");
c=os.path.dirname(__file__)
nomeArquivo=c+"\\nome.txt"

class validacpf:#validação de cpf
    def __init__(self,cpf):
        self.cpf=cpf
        print(f"cpf usado ={self.cpf}")
        self.valida()
    def valida(self):#funcão principal
        if not self.cpf:
            return False
        novo_cpf=self._calcula_digito(self.cpf[:9])  
        novo_cpf=self._calcula_digito(novo_cpf)
        
        if novo_cpf==self.cpf:
            print("valida 1 ")
            return   True
        else:
            print ("nao valida 1")
            return False
        
    @staticmethod
    def _calcula_digito(fatia_cpf):#calculo
        
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
      
class Nova_Tela:
    def __init__(self, janela):
        self.Janela = janela
        self.Tela() #chamada da Função
        self.Frames_Tela()
        self.Botoes_Tela()
        self.label()
        self.menu()
        
        self.buttonradio()  
    def validacao(self):
        cpf3=self.Nome.get()
        str(cpf3)
        print(f"cpf3: {cpf3}")
        validacpf(cpf3)
        
        if validacpf == True:
                print("cpf valido")
                return True
        else:
                print("cpf invalio")
                return False
    def Tela(self):#tela principal
        self.Janela.title("Aula 03/06/2022")
        self.Janela.configure(background="#4e5263")
        self.Janela.geometry("1000x800")
        self.Janela.resizable(True, True)
        self.Janela.maxsize(width=1000, height=800)
        self.Janela.minsize(width=600, height=400)
    def gravar_dados(self):
            self.vnome= self.Nome.get();
            self.vidade = self.idade.get();
            # self.vemail = self.email.get("1.0",END);
            nome="cola "
            matricula=654321
            idade=29
            sexo="masculino"
            mensalidade=9
            vquery =f'INSERT INTO aluno (nome,matricula,sexo,idade,mensalidade) VALUES ("{nome}",{matricula},"{sexo}",{idade},{mensalidade})'
            print("passou")
            print(vquery)
            banco1.inserirnobanco(vquery)
            # self.Nome.delete(0,END)
            # self.idade.delete(0,END)
            # self.email.delete("1.0",END)
            print("gravar dados executada")
    def semcomando(self):#funcao teste
        print("teste") 
        self.cpf= self.Nome.get();
        
    def Frames_Tela(self):#janelas ou setores dentro da tela princiapal
        self.Frame_1 = Frame(self.Janela, bg="#2e5c5a",
                            highlightbackground="#fff",
                            highlightthickness=4)#borda do frame 
        self.Frame_1.place(relx=0.00, rely=0.06, relwidth=0.99, 
                            relheight=0.46)
        self.Frame_2 = Frame(self.Janela, bg="",
                            highlightbackground="#02043d",
                            highlightthickness=2)
        self.Frame_2.place(relx=0.01, rely=0.5, relwidth=0.96, 
                            relheight=0.46)#relx=x mais em porcentagem  tudo por poecentagem
    def armazenarTXT(self):
        self.arquivo=open(nomeArquivo,"a")
        self.arquivo.write("  nome....:%s"% self.Nome.get())
        self.arquivo.write("\n idade...:%s"% self.idade.get())
        self.arquivo.write("\n email...:%s"% self.email.get())          
        self.arquivo.write("\n\n") 
        self.arquivo.close  
    def Pegar_Dados(self):
        print(f"Nome: {self.Nome.get()}")
        print(f"Idade: {self.idade.get()}")
        print(f"Observações:\n{self.email.get()}")
        self.Texto_4["text"] = self.Nome.get()
        self.Nome.delete(0,END)
        self.idade.delete(0,END)
        self.email.delete("1.0",END)
    def mostrarTXT(self):
     self.arquivo = open(nomeArquivo, 'r')
     self.conteudo = self.arquivo.readlines()
    #  self.Texto_5["text"]=self.conteudo
    def mostrarBD(self):
        vquery="SELECT * FROM aluno"
        self.Texto_5["text"]= banco1.lerdados_banco(vquery)    
       
    def grid(self):
        lista=[]
        tv=ttk.Treeview(self.Frame_1,columns=('id','nome','numero','idade','sei_nao','sexo'),show='headings')
        print("oi")
        tv.column('id',minwidth=0,width=30)
        tv.column('nome',minwidth=0,width=30)
        tv.column('numero',minwidth=0,width=30)
        tv.column('idade',minwidth=0,width=30)
        tv.column('sei_nao',minwidth=0,width=30)
        tv.column('sexo',minwidth=0,width=30)
        tv.heading('id',text='ID')
        tv.heading('nome',text='nome')
        tv.heading('numero',text='numero')
        tv.heading('idade',text='Idede')
        tv.heading('sei_nao',text='sei nao')
        tv.heading('sexo',text='sexo')
        tv.place(relx=0.01, rely=0.1,relwidth=0.9 ,relheight=0.9)
        vquery="SELECT * FROM aluno"
        v=banco1.lerdados_banco(vquery)
        print(v)
        # for f in range (6):
        #     f(str)
        print(v)
        for (id,nome,numero,sexo,idade,sei_nao) in v :
            id(str)
            idade(str)
            sei_nao(str)
            tv.insert("","end",values=(id(str),nome,numero,sexo,idade(str),sei_nao(str)))
        
    def update_banco_tela(self):
        nome="cola "
        Data="2012-04-03"
        quant=1220
        matricula=654321
        idade=29
        sexo="masculino"
        mensalidade=9
        p=1
        vquery=f"UPDATE aluno SET nome ='{nome}',matricula={matricula},sexo='{sexo}',idade={idade},mensalidade={mensalidade} where id_aluno = {p}"
        banco1.update_banco(vquery)    
    def delete_banco_tela(self):
        produto=3
        vquery=f"DELETE FROM aluno WHERE  id_aluno={3}"
        print(f"xoi")
        banco1.delete_banco(vquery)     
    def menu(self):
        barrademenu=Menu(self.Frame_2)#adivinhaa

        menucomtatos=Menu(barrademenu,tearoff=0)#opicao do menu 

        menucomtatos.add_command(label="novo",command=self.grid)
        menucomtatos.add_command(label="pesquisa",command=self.pesquisa)
        menucomtatos.add_command(label="deletar",command=self.semcomando)
        menucomtatos.add_separator()#separacao 
        menucomtatos.add_command(label="fechar",command=Janela.quit)#fechara a janela
        barrademenu.add_cascade(label="contados",menu=menucomtatos)#acrecentando na funcao barramenu(importante)

        menumanutencao=Menu(barrademenu,tearoff=0)
        menumanutencao.add_command(label="Banco de dados",command=self.semcomando)
        barrademenu.add_cascade(label="manutencao",menu=menumanutencao)
        menusobre=Menu(barrademenu,tearoff=0)
        menusobre.add_command(label="cfb",command=self.semcomando)
        barrademenu.add_cascade(label="sobre",menu=menusobre)#nao se esqueca desse menu(menu=)

        Janela.config(menu=barrademenu)  
    def label(self):
        self.Texto_3 = Label(self.Frame_1, bg="#570318", fg="#000")
        self.Texto_3["text"] = "nome"
        self.Texto_3["font"] = ("Arial", "14", "bold")#especificacoe do texto
        self.Texto_3.place(relx=0.01, rely=0.1,relwidth=0.1 ,relheight=0.1)
        
        self.Nome = Entry (self.Frame_1)
        self.Nome["font"] = ("Arial", "14", "bold")
        self.Nome.place(relx=0.03, rely=0.2,relwidth=0.2, relheight=0.2)
        
        self.Texto_2 = Label(self.Frame_1, bg="#570318", fg="#000")
        self.Texto_2["text"] = "idade"
        self.Texto_2["font"] = ("Arial", "14", "bold")#especificacoe do texto
        self.Texto_2.place(relx=0.01, rely=0.5,relwidth=0.1 ,relheight=0.1)
        self.idade =Entry(self.Frame_1)
        self.idade["font"] = ("Arial", "14", "bold")
        self.idade.place(relx=0.03, rely=0.6,relwidth=0.2, relheight=0.2)
        
        self.Texto_1 = Label(self.Frame_1, bg="#570318", fg="#000")
        self.Texto_1["text"] = "email"
        self.Texto_1["font"] = ("Arial", "14", "bold")#especificacoe do texto
        self.Texto_1.place(relx=0.25, rely=0.5,relwidth=0.1 ,relheight=0.1)
        self.email = Text(self.Frame_1)
        self.email["font"] = ("Arial", "14", "bold")
        self.email.place(relx=0.27, rely=0.6,relwidth=0.2, relheight=0.2)  
        
        self.Texto_4 = Label(self.Frame_2, bg="#570318", fg="#000")
        self.Texto_4["text"] =""#especificacoe do texto
        self.Texto_4["font"] = ("Arial", "14", "bold")#especificacoe do texto
        self.Texto_4.place(relx=0.01, rely=0.2,relwidth=0.2 ,relheight=0.3)
        self.Texto_5 = Label(self.Frame_2, bg="#570318", fg="#000")
        self.Texto_5["text"] =""#especificacoe do texto
        self.Texto_5["font"] = ("Arial", "11", "bold")#especificacoe do texto
        self.Texto_5.place(relx=0.55, rely=0.01,relwidth=0.44 ,relheight=0.9)
        self.Texto_1 = Label(self.Frame_1, bg="#570318", fg="#000")
        self.Texto_1["text"] = "sexo"
        self.Texto_1["font"] = ("Arial", "14", "bold")#especificacoe do texto
        self.Texto_1.place(relx=0.25, rely=0.1,relwidth=0.1 ,relheight=0.1)
        self.sexo = Text(self.Frame_1)
        self.sexo["font"] = ("Arial", "14", "bold")
        self.sexo.place(relx=0.25, rely=0.2,relwidth=0.2, relheight=0.2) 

        
    def Botoes_Tela(self):#butoes
        self.Botao_1 = Button(self.Frame_1)#localizacao para seus parametros
        self.Botao_1["text"] = "Fechar"
        self.Botao_1["font"] = ("Arial", "12", "bold")#especificacoe do texto
        self.Botao_1["command"] = self.validacao
        self.Botao_1.place(relx=0.9, rely=0.0,relwidth=0.1, relheight=0.15)
        
        self.Botao_2 = Button(self.Frame_2)
        self.Botao_2["text"] = "nova aba"
        self.Botao_2["font"] = ("Arial", "12", "italic")
        self.Botao_2["command"] = self.Nova_Janela
        self.Botao_2.place(relx=0.1, rely=0.0,relwidth=0.1, relheight=0.15)
        
        self.Botao_3 = Button(self.Frame_2)
        self.Botao_3["text"] = "pegar"
        self.Botao_3["font"] = ("Arial", "12", "italic")
        self.Botao_3["command"] =  self.Pegar_Dados
        
        self.Botao_3.place(relx=0.00, rely=0.01,relwidth=0.1, relheight=0.15)
        self.Botao_3 = Button(self.Frame_2)
        self.Botao_3["text"] = "armazenar"
        self.Botao_3["font"] = ("Arial", "12", "italic")
        self.Botao_3["command"] = self.armazenarTXT
        
        self.Botao_3.place(relx=0.4, rely=0.01,relwidth=0.15, relheight=0.15)
        self.Botao_4= Button(self.Frame_2)
        self.Botao_4["text"] = "mostrar"
        self.Botao_4["font"] = ("Arial", "12", "italic")
        self.Botao_4["command"] = self.mostrarBD
        
        self.Botao_4.place(relx=0.5, rely=0.5,relwidth=0.15, relheight=0.15)
        self.Botao_5= Button(self.Frame_2)
        self.Botao_5["text"] = "banco de dados"
        self.Botao_5["font"] = ("Arial", "12", "italic")
        self.Botao_5["command"] = self.delete_banco_tela
        self.Botao_5.place(relx=0.4, rely=0.2,relwidth=0.15, relheight=0.15)
    def buttonradio(self):
        self.verdominio=StringVar()
        self.Texto_9 = Label(self.Frame_1, bg="#570318", fg="#000")
        self.Texto_9["text"] = "dominio"
        self.Texto_9["font"] = ("Arial", "14", "bold")
        self.Texto_9.place(relx=0.5, rely=0.02,relwidth=0.2 ,relheight=0.1)
        self.dominio_adm=Radiobutton(self.Frame_1,text="adm",value="e",variable=self.verdominio)
        self.dominio_adm.place(relx=0.5, rely=0.1,relwidth=0.1 ,relheight=0.1)
        self.dominio_aluno=Radiobutton(self.Frame_1,text="aluno",value="u",variable=self.verdominio)
        self.dominio_aluno.place(relx=0.5, rely=0.2,relwidth=0.1 ,relheight=0.1)
        self.dominio_funcionario=Radiobutton(self.Frame_1,text="funcionario",value="w",variable=self.verdominio)
        self.dominio_funcionario.place(relx=0.5, rely=0.3,relwidth=0.1 ,relheight=0.1)
        self.btn_domominio=Button(self.Frame_1,text="dominio selecionado",command=self.inprimirdominio)
        self.btn_domominio.place(relx=0.5, rely=0.4,relwidth=0.2 ,relheight=0.1)

    def inprimirdominio(self): 
        self.ve=self.verdominio.get()
        print(self.ve)
        if self.ve=="e":
            print("ele serar um adm")
        elif self.ve=="w":
            print("ele serar um funcionario")
        elif self.ve=="u":
            print("ele serar um aluno")
        else:
            print("escolha um dominio")
    def Nova_Janela(self):#criar nova janela 
        self.Janela_2 = Toplevel()
        self.Janela_2.title("Nova Janela")
        self.Janela_2.geometry("300x300")
        self.Janela_2.configure(background="#000")
        self.Janela_2.resizable(False, False)
        self.Janela_2.transient(self.Janela)
        self.Janela_2.focus_force()
        self.Janela_2.grab_set()
        self.Texto_3 = Label(self.Janela_2, bg="#570318", fg="#000")
        self.Texto_3["text"] = "cadastro efetuado"
        self.Texto_3["font"] = ("Arial", "14", "bold")
        self.Texto_3.place(relx=0.05, rely=0.1,relwidth=0.4 ,relheight=0.4)
    def pesquisa(self):#criar nova janela 
        self.Janela_3 = Toplevel()
        self.Janela_3.title("Nova Janela")
        self.Janela_3.geometry("600x600")
        self.Janela_3.configure(background="#000")
        # self.Janela_3.resizable(False, False)
        self.Janela_3.transient(self.Janela)
        self.Janela_3.focus_force()
        self.Janela_3.grab_set()
        self.Texto_9= Label(self.Janela_3, bg="#570318", fg="#000")
        self.Texto_9["text"] = "manipulaaao do banco"
        self.Texto_9["font"] = ("Arial", "14", "bold")
        self.Texto_9.place(relx=0.00, rely=0.0,relwidth=0.99 ,relheight=0.1)  
Janela = Tk()
Nova_Tela(Janela)
Janela.mainloop()