from time import sleep
from random import randint
p=0
x=randint(1,10)
print(x)
print('-=-'*20)
print("pensei em um numero, tente acertar")
f=int(input("qual numero voce acha que e : "))
print('-=-'*20)
print("procesando...")
sleep(2)
acertou = False
while not acertou:
        print("nao e esse:")
        f=int(input("tente de novo qual o numero que voce acha:"))
        p+=1
        if f == x:
                acertou= True
        else:
                if f<x:
                        print('maior... tente mais uma vez')
                elif f>x:
                        print('menor... tente mais uma vez')
print('-=-'*20)
print("voce acertou o valor era {} voce tentol {}".format(x,p))


