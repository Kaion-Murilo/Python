from os import remove
from random import randint, random,choice,shuffle
nome=[]
for i  in range (4):
    nome1=str(input("digiti o nome: "))
    nome.append(nome1)
print(nome)
f=3
g=1
# for o in range(3):
#     s=randint(0,f)   
#     nome1=choice(nome)
#     print("o {} grupo a apresentar e  {} ".format(g,nome1))
#     nome.remove(nome1)
#     print(nome)
#     f=f-1
#     g=g+1
# print("o {} grupo a apresentar e  {} ".format(g,nome[0]))

shuffle(nome)
print(f"A orden sera de {nome}")