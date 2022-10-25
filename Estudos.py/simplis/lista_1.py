
import os

os.system("cls");
'''
valor=[]
valor.append(input('escreva o digito'))
valor.append(input('escreva o digito'))
valor.append(input('escreva o digito'))
valor.append(input('escreva o digito'))
valor.append(input('escreva o digito'))
print(valor)
valor.sort
print(valor[0])
print(valor[4]) 


d=0
a=0
d=int(input('digiti qual tabuada deseja 1=mult 2=div 3=soma 4=subt'))
valor = int(input('Entre com um número para saber a tabuada: '))  
aux = 0  
print('*' * 18)  
print('Tabuada de {}'.format(valor))  
print('*' * 18) 
if d==1:
 while(aux <= 10):  
  print('{0} X {1} = {2}'.format(aux, valor, (aux * valor)))  
  aux = aux + 1 
elif d==2:
 while(aux <= 10):  
  print('{0} / {1} = {2}'.format(aux, valor, (aux / valor)))  
  aux = aux + 1
elif d==3:
   while(aux <= 10):  
    print('{0} +{1} = {2}'.format(aux, valor, (aux + valor)))  
    aux = aux + 1 
elif d==4:
   while(aux <= 10):  
    print('{0} - {1} = {2}'.format(aux, valor, (aux - valor)))  
    aux = aux + 1 

vet=[]
i= int(input('escreva  o valor de i:'))
vet.append(input('escreva  o valor de i:'))
vet.append(input('escreva  o valor de i:'))
vet.append(input('escreva  o valor de i:'))    
if i==1:
 vet.sort()
 print(vet)
elif i ==2:
 vet.reverse()
 print(vet)
elif i ==3: 
    vet.sort
    x=vet[2]
    y=vet[1]
    vet[1]=x
    vet[2]=y
    print(vet)

a=[]
x=0
y=2
while x!=y*2:
 y=x
 x=int(input('escreva o a'))
 a.append([x])

 print(x)
 print(y)
print(a)


o=0
a=[]
x=0
for i in range (10):
 x=int(input('escreva o a'))
 a.append([x])
 if x%2==0:
      o=o+1
print(o)
print(a)
a.sort()
print(a[0])
print(a[9])
'''