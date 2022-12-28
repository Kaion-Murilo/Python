jogador = dict()
partidas= list()
jogador['nome'] = str(input("nome do jogador: "))
tot = int(input(f"Quantos patidas {jogador['nome']} jogou?"))
for c in range (0,tot):
    partidas.append(int(input(f"     Quantas gols na partida {c}?")))
jogador["gols"]= partidas[:]
jogador["total"] = sum(partidas)
print("=-"*30)
print(jogador)
print("=-"*30)
for k,v in jogador.items():
    print(f"O campo {k} tem o valor {v} gols")
print("=-"*30)
print(f"O jagador {jogador['nome']} jogou {len(jogador['gols'])} partidas.")
for i,v in enumerate(jogador["gols"]):
    print(f"         =>   partidas {i}, fez {v} gols.")
print(f"For um total de {jogador['total']} gols")