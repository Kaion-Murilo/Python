times = list()
jogador = dict()
partidas= list()
while True:
    jogador.clear()
    jogador['nome'] = str(input("nome do jogador: "))
    tot = int(input(f"Quantos patidas {jogador['nome']} jogou?"))
    partidas.clear()
    for c in range (0,tot):
        partidas.append(int(input(f"     Quantas gols na partida {c+1}?")))
    jogador["gols"]= partidas[:]
    jogador["total"] = sum(partidas)
    times.append(jogador.copy())
    while True:
        resp= str(input("quer continuar ?")).upper()[0]
        if resp in "SnsN":
            break
        print("erro! por favor , digiti certo")
    if resp == "N":
        break 
print("=-"*30)
print('cod ',end="")
for i in jogador.keys():
    print(f"{i:<15}",end='')
print()
print("=-"*40)
for k,v in enumerate(times):
    print(f"{k:>3}  ", end="")
    for d in v.values():
        print(f"{str(d):15}", end='')
    print()
print('-'*40)
while True:
    busca = int(input("mostrar dados de qual jogador ?"))
    if busca == 999 :
        break
    if busca>= len(times):
        print(f"erro digiti certo nao existe esse cod de {busca}")
    else:
        print(f" - ---lavenatamento do jogador {times[busca]['nome']}")
        for i,g in enumerate (times[busca]["gols"]):
            print(f"       No jogo {i+1} fez {g} gols")
    print("-"*40)
print("FIM")