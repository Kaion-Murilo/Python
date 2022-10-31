from datetime import date
maior=[]
memor=[]
anos=[]
a=0
b=0
for i in range (7):
    x= int(input("DIGITI O ANO DE NACIMENTO: "))
    ano= date.today().year 
    print(ano)
    print(x)
    idade=ano-x
    maior.append(x)
    memor.append(x-ano)
    if idade <=21:
       a=1+a 
       print(a)
    elif idade>=21:
       b=1+b
       print(b)
    
print(f"O NUMERO DE PESSOAS MENORES E DE  {b} :")
print(f"O NUMERO DE PESSOAS DDE MAIOR DE 21 {a}:")
print(maior)
print(memor)