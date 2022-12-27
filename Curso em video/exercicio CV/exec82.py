num = list()
pares = list()
impares = list()
while True:
    num.append(int(input("digiti os  valors:")))
    resp=str(input("Quer continuar?[S/N]"))
    if resp in "Nn":
        break
for i,v in enumerate(num):
    if v % 2 ==0:
        pares.append(v)
    elif v%2==1:
        impares.append(v)
print("=-"*30)
print(f'A lista completa {num}')
print(f'A lista de pares {pares}')
print(f'A lista de inpares {impares}')