import os
os.system("cls");
"""
a=0
b=0
def mostralinha():
    print('----------------------------------------')
mostralinha()
print('sistema de aluno')
mostralinha()
mostralinha()
print('soma')
mostralinha()

def titulo(txt):
 print('-'*30)
 print(txt)
 print("-"*30)
titulo('sistema')
titulo("aprende")
titulo('sistema de aluno')

def soma(a,b):
    print(f"A={a} e B={b}")
    s=a+b
    print(f'a soma de A+B ={s}')
soma(b=4,a=50)
soma(2,1)
soma(6,4)

def contador(*num):
    for valor in num:
        print(f'{valor}',end='')
    print('fim!')

def contador(*num):
    tam=len(num)
    print(f"recebito os valores {num} e sao ao todos {tam} numero")
contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)

def dobra(lst):
    pos=0
    while pos< len(lst):
        lst[pos] *=2
        pos+=1
valores= [5,43,2,2,6,7,9,10]
dobra (valores)
print(valores)

def soma(*valores):
       s=0
       for num in valores:
        s+=num
       print(f"sama  de valores {valores} temos {s}")  
soma(5,2)
soma(2,9,4,5)
soma(19,4,2,2,)

def soma(a=0,b=0,c=0):
    s=a+b+c
    print(f"a soma e {s}")
soma()
soma(1,2)
"""
def soma(a=0,b=0,c=0):
    s=a+b+c
    return s
r1=soma(3,2,5)
r2=soma(1,2)
print(f"os resultados foram {r1} e {r2}")
