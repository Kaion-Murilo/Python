from time import sleep
from random import randint
print('-=-'*20)

itens = ('pedra', ' papel ' , 'tisolra')
computador=randint(0 , 2)
print('O computador jogol {}'.format(itens[computador]))
print('-=-'*20)
jogador=int(input('''
[ 0 ] = pedra 
[ 2 ] = papel  
[ 3 ] = tisolra 
digiti sua forma: '''))
print("jo")
sleep(1)
print("ken")
sleep(1)
print("po!!")
sleep(1)
print('-=-'*20)
print('O computador jogol {}'.format(itens[computador]))
print('O jogador jogol {}'.format(itens[jogador]))
print('-=-'*20)
if computador == 0 :
    if jogador == 0:
        print("enpate")
    elif jogador == 1:
        print("jogaddor vencel")
    elif jogador == 2:
        print("computador vencel")
    else:
         print("jogada  invalida")
elif computador == 1 :
    if jogador == 0:
       print("computador vencel") 
    elif jogador == 1:
        print("enpate")   
    elif jogador == 2:
        print("jogaddor vencel")
    else:
         print("jogada  invalida")
elif computador == 2 :
    if jogador == 0: 
        print("jogaddor vencel")
    elif jogador == 1:
        print("computador vencel")
    elif jogador == 2:
        print("enpate")   
    else:
        print("jogada  invalida")
print('-=-'*20)