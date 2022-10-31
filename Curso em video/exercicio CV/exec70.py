preco=tot=cont=acu=0
nomemenor=""
while True:
    nome= str(input("digiti  nome do produto : ")).upper().strip()
    preco= float(input("digiti o preço:"))
    cont+=1
    tot += preco
    if cont == 1 or preco<menor:
        menor=preco
        nomemenor=nome    
    if preco>1000:
        acu+=1
    dec=" "
    while dec not in "SN":
        dec=str(input("deseja contunuar sim ou nao: ")).upper().strip()[0]
    if dec =='N':
        break
print("{:-^40}".format("FIM DO PROGGRAMA"))
print(f"preco total :{tot} ")
print(f"{acu } produtos que passaram de R$1000")
print(f'menor produto nome: {nomemenor} com preco de  {menor}')
