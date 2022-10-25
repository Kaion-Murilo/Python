
import os
os.system("cls");
'''
k=0
while k != 1:

 lis=[]
 for c in range (0,5):
    lis.append(int(input(f'figiti um valor da posicao {c}:')))
    if c==0:
       mai=men=lis[c]
    else:
      if lis[c]>mai:
         mai=lis[c]
      if lis[c]<men:
         men=lis[c]
 print('=-'*30)
 print(f'vocr  digitou os valores{lis}')
 print(f'maior valor digitado{mai}')
 print(f'menor valor digitado{men}')
 print('o maior valor estar localizado na possssicao:',lis.index(mai))
 print('o menor valor estar localizado na possssicao:',lis.index(men))
 k=int(input("deseja sair entao digiyi 1 senao digiti 2")) 

lis=[]
i=int
j=int
x=int
j=int
for i in range (0,5):
    lis.append(input('adicione um valor'))
    
print(lis)
h=lis[::-1]
print(h)
lis.reverse()
print(lis)

#revisar
m=[0,0,0],[0,0,0],[0,0,0]
for i in range (0,3):
   for c in range (0,3):
      m[i][c]=int(input(f'escreva o valo que ficarar na posicao {i}{c}'))
print(m)
for l in range (0,len(m),1):
   for j in range (0,len(m),1):
    print(f'[{m [l][j]:^5}]',end='-')
   print()
d=m[0][0]+m[1][1]+m[2][2]
print(f'este e valor da diagonal {d}')

m=[[0,0,0,0,0,0]
 , [0,0,0,0,0,0]
  ,[0,0,0,0,0,0]]
for i in range (0,3):
   for c in range (0,6):
      m[i][c]=int(input(f'escreva o valo que ficarar na posicao {i}{c}'))
print(m)
for l in range (0,3,1):
   for c in range (0,6,1):
    print(f'[{m [l][c]:^5}]',end='-')
   print()

a=m[0][1]+m[1][1]+m[2][1]+m[0][3]+m[1][3]+m[2][3]+m[0][5]+m[1][5]+m[2][5]
print(a)

l=m[0][2]+m[1][2]+m[2][2]+m[0][4]+m[1][4]+m[2][4]
b=l/6
print(f"este e a media:{b}")

m[0][5]=m[0][1]+m[0][2]
m[1][5]=m[1][1]+m[1][2]
m[2][5]=m[2][1]+m[2][2]
print('=-'*30)
for l in range (0,3,1):
   for c in range (0,6,1):
    print(f'[{m [l][c]:^5}]',end='-')
   print()

mts=[],[]#quase isso 
lis=[],[]
i=0
n=int
x=0
j=int
x =int( input("Digite um valor inteiro positivo: "))
j=x
for i in range (j):
 if i % 2 ==0:
    lis[0].append(i)
 else:
    lis[1].append(i)
print(mts)
print(f'numeros pares{lis}')

--------------------------------------===--

i == 0
valor =0
n=0
valor= int(input('digito'))
while (i < n):
   valor <- valor + ((-1 ^ i) / (2 * i + 1))
   i <- i + 1
x=valor*4
print(x)
print(valor * 4)

----------------------------------------------------------

while True:
 x=str(input('Digite um numero inteiro positivo e maior que 0: '))
 if x.isnumeric():
  x = int(x)
 if x>0:
  break
print(f'"{x}" não atende às condições impostas!\n')
print('Intervalo: ', end='')
for c in range(0, x+1):
 print(c, end=' ')

vet=[]
dp=[]
m=0
c=0
i=0
for i in range (0,5):
   vet.append(int(input(f'digiti o valor da posicao {i}')))
   m=m+vet[i]
print(vet)
mg=m/5
print (mg)
for c in range (0,5):
 h=vet[c]-mg
 dp.append(h)
 print('dp:',dp)
v=dp[0]*dp[0]+dp[1]*dp[1]+dp[2]*dp[2]+dp[3]*dp[3]+dp[4]*dp[4]
print('aqui v :',v)
f=v/5
#dpg=f**(1/2)
print('**',f)

from math import *
def f(x):
   f=x**3-9*x+3
   return f
def dnf(x):
    h=1e-8
    dnf=(f(x+h)-f(x))/h
    return dnf
x=0
tol=1e-6
k=0
while abs(f(x))> tol:
   print(k,x,f(x))
   x=x-f(x)/dnf(x)
   k+=1
print(k,x,f(x))
print('resultado e:',x)
=====================================================================================
def definirBandeira(card):
    if card[0] == 3:
        amEx = [4, 7]
        if card[1] in amEx:
            return 'American Express'
        else:
            return 'Outra Bandeira'
    elif card[0] == 4:
        return 'Visa'
    elif card[0] == 5:
        mstC = [1, 2, 3, 4, 5]
        maes1 = [0, 6, 7, 8, 9]
        if card[1] in mstC:
            return 'Master Card'
        elif card[1] in maes1:
            return 'Maestro'
    elif card[0] == 6:
        maes2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if card[1] in maes2:
            return 'Maestro'
    else:
        return 'Outra Bandeira'

def dígitoVerificador(card):
    soma = 0
    for i in range(len(card)):
        if i % 2 == 0:
            card[i] *= 2
            if card[i] > 9:
                aux0 = str(card[i])
                aux1 = int(aux0[0])
                aux2 = int(aux0[1])
                card[i] = aux1 + aux2
            soma += card[i]
        else:
            if i < len(card)-1:
                soma += card[i]
    ctrl = 1
    dV = 0
    while soma % 10 != 0:
        soma += ctrl
        dV += 1
    return dV

os.system('cls')

cartão = []

while True:
    for i in range(0, 16):
        cartão.append(int(input('> ')))

    print(f'Bandeira do Cartão: {definirBandeira(cartão[:])}')
    print(f'Dígito verificador: {dígitoVerificador(cartão[:])}')
    print(f'Cartão válido: {dígitoVerificador(cartão[:]) == cartão[-1]}')

    op = input('Continuar? [S|N]: ')
    if op.upper() == 'N':
        break
        =================================================================================
'''
car=[]
for i in range(0,16,1):
 car.append(int(input(f"digiti onumeros do cartao{i}::")))
x=car[0]
if (x<=6):
    print("cartao errado ")
elif x<3:
   print("cartao errado ")
print( car)
print("=-"*30)
if car[0]==4:
 print("o cartao e visa")
elif ((51==car[0]) or (car[0]==55)):
   print("mastercard")
elif ((37==car[0]) or (car[0]==34)):
   print(" American Express ")
elif ((59<=car[0]) and (car[0]<69)): 
   print("Maestro")
elif  car[0]==50:
   print("Maestro")
else:
   print("cartao nao encontrado")
print("=-"*30)
car[0]=car[0]*2
car[2]=car[2]*2
car[4]=car[4]*2
print(f" o vetro {car}")
vet=[]

print(vet)
