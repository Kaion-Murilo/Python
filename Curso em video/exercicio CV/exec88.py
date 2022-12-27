from random import randint
lista= []
jogos= []
print('-'*30)
print("              JOGO NA MEGA SENA             ")
print('-'*30)
quant = int (input("quantos jogos voce quer que eu sortei?"))
tot=1
while tot <=quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont >=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot +=1
print('-='*3,F"SORTEANDO {quant} JOGOS","=-"*3)
for i,l in enumerate(jogos):
    print(f"jogo {i+1}:{l}")