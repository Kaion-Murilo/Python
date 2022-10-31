from time import sleep
from random import randint

x=randint(1,5)
print(x)
print('-=-'*20)
print("pensei em um numero, tente acertar")
f=int(input("qual numero voce acha que e : "))
print('-=-'*20)
print("procesando...")
sleep(2)
if x==f:
    print("voce acertou o valor era {}".format(x))
else:
    print("desculpa voce errou o sumero era {}".format(x))
print('-=-'*20)