from random import randint, random,choice

nome=[]
for i  in range (4):
    nome1=str(input("digiti o nome: "))
    nome.append(nome1)
print(nome)
# s=ra(0,3)
print("o aluno escolhido foi o {} ".format(choice(nome)))