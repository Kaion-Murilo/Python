f = 0
somaidade = 0
nomevelho = 0
idadevelho = 0
somaidade = 0
for i in range(4):
    print("----------------[ {} ] PESSOA----------".format(i))
    nome = str(input("DIGITI NOME:")).upper().strip()
    idade = int(input("DIGITI IDADE:"))
    sexo = str(input("DIGITI SEXO [M/F]:")).upper()
    somaidade=idade+somaidade
    if idade >idadevelho:
        idadevelho=idade
        nomevelho =nome
    if sexo in "Ff" and idade<20:
        f=f+1
print(f'a idade media :{somaidade/4}')
print(f"pessoa mais  velha {nomevelho} com {idadevelho}")
print(F'numero de meninas com menos de 20 e : {f}')