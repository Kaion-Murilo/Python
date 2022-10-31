import os
from statistics import median
os.system("cls");
'''
p = int(input('escreva o numero do indice de poluicao'))
print(p)
if p==3:
   print("desative o primeiro grupo")
elif (p<=4) and p>3:
 print('desative o 1 e2 grupo ')
elif p>=5:
 print('desative o todos os grupo ')
else :
 print('oi')
 --------------------------------------

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

aux=0
l=0
m1=(input('digiti o peso'))
if m1>=90:
 l=l+1
m2=(input('digiti o peso'))
if m2>=90:
 l=l+1
m3=(input('digiti o peso'))
if m3>=90:
 l=l+1
m4=(input('digiti o peso'))
if m4>=90:
 l=l+1
m5=(input('digiti o peso'))
if m5>=90:
 l=l+1
m6=(input('digiti o peso'))
if m6>=90:
 l=l+1
m7=(input('digiti o peso'))
if m7>=90:
 l=l+1
media=m1+m2+m3+m4+m5+m6+m7
media1=media/7
print(media1)
print(l)

m=[]
i=0
media=0
l=0
for i in range (7):
  m.append(int(input("digiti o peso")))
  media=m[i]+ media
  if m[i]>90:
   l=l+1
print(media)
media1=media/7
print(media1)
print(l)

 max_value = max(x)
 print('Maximum value:', max_value)
 mam_value = min(x)
 print('Maximum value:', mam_value)
 print(x.index(max_value))
 print(x.index(mam_value))
 print(f"este foi o maior valor {mai}")
  print(f"este foi o menir valor {min}")
  
  k=0 #m ap sei 
mai=mini=0
while k!=1:
  x=[]
  for i in range (0,9):
     x.append(int(input(f'escreva volores posicao {i}:   ')))
     if i ==0:
        i =0
     else :
        if x[i]>mai:
         x[i]=mai
        if x[i]<mini:
         x[i]=mini
  print('=-'*30)
  print(x)

  k=int(input("deseja sair entao digiyi 1 senao digiti 2")) 

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
'''
matriz=[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]
for i in range (0,5,1):
  for j in range(0,5,1):
      matriz[i][j]=int(input("digiti o valor:"))
      print(matriz)
print(matriz)
r=0
g=0
media=0
while r!=5:
    r=1+r
    g=g+1
    media+=matriz[r][g]
    print(matriz[r][g])   
    
mediaaritimedica=media/5
print(mediaaritimedica)
