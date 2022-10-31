a=0
b=0
dec=" "
acu=0
meni=0
masac=0
while True:
    idade= int(input("digiti seu  idade : "))
    sexo=" "
    while sexo not in "MFmf":
        sexo= str(input("digitiseu sexo [M] ou [F]:")).upper().strip()
    if idade>18:
        acu+=1
    if sexo in ("Mm"):
        masac+=1
    if sexo in ("Ff") and idade<=20:
        meni+=1
    
    dec=" "
    while dec not in "NS":
        dec=str(input("deseja contunuar sim ou nao: ")).upper().strip()
    if dec == 'N':
        break

print(f"pessoas com mais de 18 anos {acu}")
print(f'pessoa s com sexo masculino {masac}')
print(f'meninas com menos de 20 anos  {meni}')