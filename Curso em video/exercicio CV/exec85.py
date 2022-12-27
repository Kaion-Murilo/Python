valores=[]
#0= pares 1 = impares
pares=[]
impares=[]
for i in range(0,7):
    valor=int(input(f"digiti o valor de posicao {i}: "))
    if valor % 2 ==0:
        pares.append(valor)
    elif valor%2==1:
        impares.append(valor)
pares.sort()
impares.sort()
valores.append(pares[:])        
valores.append(impares[:])        
print(valores)
print(f"{valores}")