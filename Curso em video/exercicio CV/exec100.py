from random import randint
from time import sleep


def sorteio(lista):
    print("sortei de 5 valores de lista :  ",end='')
    for cont in range(0,5):
        n=randint(1,10)
        lista.append(n)
        print(f"{n},",end='', flush=True)
        sleep(0.3)
        
    print("PRONTO.")

def somarPAR(lista):
    soma=0
    for valor in lista:
        if valor %2 ==0:
            soma += valor
        print(f"Soma os valors de {lista}, temos {soma}")
numeros = list()
sorteio(numeros)
somarPAR(numeros)