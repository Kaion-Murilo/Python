import os
os.system("cls");
import os
from tkinter import *
import carrinhodeconpra as car
import produto as pro
# adicionar arqquivo txt
c=os.path.dirname(__file__)
nomeArquivo=c+"\\conpra.txt"
# continua no def mostrarcarrinho

carrinho = car.CarrinhoDeCompras()
p1 = pro.Produto('PlayStation 5', 5000)
p2 = pro.Produto('Caderno', 15)
p3 = pro.Produto('MacBook', 30000)
p4 = pro.Produto('Iphone', 13000)

carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p2)
carrinho.inserir_produtos(p3)
carrinho.inserir_produtos(p4)

carrinho.listar_produtos()
def inserirproduto():
    produto_inf = produto.get();
    valor_inf = valor.get();
    print(f"produto: {produto_inf}")
    print(f"valor: {valor_inf}")
    Texto_6["text"]= f"nome:{produto_inf}---valor:{valor_inf}"
def armazenar():
    arquivo=open(nomeArquivo,"a")
    arquivo.write("   produto...:%s"%  produto.get())         
    arquivo.write("\n +valor....:%s"%  valor.get())
    arquivo.write("") 
    arquivo.close   
def mostrarcarrinho():
     arquivo = open(nomeArquivo, 'r')
     conteudo = arquivo.readlines()
     Texto_7["text"]=conteudo
     []
     arquivo.close   
Janela = Tk()
Janela.title("compra - 27/05/22")
Janela.geometry("1010x7000")
Janela.configure(background="#55626b")

Texto_1 = Label(Janela, text="Aula 1 de Interface Gráfica - 27/05/2055", background="#d16704", foreground="#fa05d9")
Texto_1.place(x=10, y=20, width=250, height=20)

teste = "Utilizando o TKinter!"
cor_bg = "#fff"
cor_fg = "#689"
Texto_2 = Label(Janela, text= teste, background=cor_bg, foreground=cor_fg)
Texto_2.place(x=10, y=45, width=250, height=20)

Texto_3 = Label(Janela, text="produto", background="#fff", foreground="#000")
Texto_3.place(x=20, y=70, width=70, height=30)
produto = Entry(Janela)
produto.place(x=90, y=70, width=200, height=30)

Texto_4 = Label(Janela, text="valor", background="#fff", foreground="#000")
Texto_4.place(x=20, y=105, width=70, height=30)
valor = Entry(Janela)
valor.place(x=90, y=105, width=200, height=30)

x=carrinho.listar_produtos()
Botao_1 = Button(Janela, text="dados inseridos", command=inserirproduto, background="#00f", foreground="#fff")
Botao_1.place(x=70, y=260, width=70, height=30)
Botao_1 = Button(Janela, text="armazenamento", command=armazenar, background="#00f", foreground="#fff")
Botao_1.place(x=190, y=260, width=70, height=30)
Texto_6 = Label(Janela, text="", background="#fff", foreground="#000")
Texto_6.place(x=300, y=80, width=200, height=80)
Texto_7 = Label(Janela, text="", background="#fff", foreground="#000")
Texto_7.place(x=600, y=80, width=400, height=470)
Botao_3 = Button(Janela, text="print", command=mostrarcarrinho, background="#00f", foreground="#fff")
Botao_3.place(x=279, y=260, width=70, height=30)
Janela.mainloop()