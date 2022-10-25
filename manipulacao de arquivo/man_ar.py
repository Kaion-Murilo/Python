import os
os.system("cls");
#0 r e leitura e w para escreta.

a=(input("aqui e foda :>="))
arquivo=open('textoo.txt','r')
conteudo=arquivo.read()
print(conteudo)


print("abri  arquivo ")
linha="."
while linha != "":
    linha=arquivo.readline()
print(linha)
arquivo=input("digiti o nome do arquivo:")
arq= open(arquivo,'r')
for i in range (0,5,1):
    print(arq.readline().strip())
arq.close()

#Ler um arquivo criado previamente e exibir as suas 5 primeiras linhas.
arquivo = input("Digite o nome do teu arquivo: ")
arq = open(arquivo, "r")
for i in range(6):
  print(arq.readline().strip())
arq.close()

#Ler um arquivo e exibir a quantidade de palavras presentes no arquivo.
arquivo = input("Digite o teu arquivo, faz favor: ")
arq = open(arquivo, "r")
#contar as palavras em cada linha
cont = 0
#lendo linha por linha
for palavras in arq:
  cont += len(palavras.split(' '))
print(f"O número de palavras é: {cont}.")
arq.close()