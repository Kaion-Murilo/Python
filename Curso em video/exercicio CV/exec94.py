galera = list()
pessoa = dict()
soma=media=0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input("Nome: "))
    while True:
        pessoa["sexo"]=str(input("sexo:  [M/F]")).upper()[0]
        if pessoa["sexo"] in "MF":
            break
        print("erro! por favor , digiti certo")
    pessoa["idade"]= int(input("idade: "))
    soma += pessoa["idade"]
    galera.append(pessoa.copy())
    while True:
        resp= str(input("quer continuar ?")).upper()[0]
        if resp in "SnsN":
            break
        print("erro! por favor , digiti certo")
    if resp == "N":
        break
print("=-"*30)
print(f"A) Ao todo temos {len(galera)} pessoa cadastrado")
media = soma / len(galera)
print(f"B) media iadade e de {media:5.2f} anos.")
print("C)As mulheres cadastradas foram ",end="")
for p in galera:
    if p["sexo"] in "Ff":
        print(f"{p['nome']} " , end="")
print()
print("D) Lista das pessoas que estao acima da media : ")
for p in galera:
    if p["idade"]>= media:
        print("  ",end="")
        for k,v in p.items():
            print(f"{k} = {v}; ",end="")
        print()
print("<<ENCERRRA>>")