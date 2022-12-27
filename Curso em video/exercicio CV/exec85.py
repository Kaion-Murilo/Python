valores=[[],[]]
#0= pares 1 = impares
valor=0
for i in range(0,7):
    valor=int(input(f"digiti o valor de posicao {i}: "))
    if valor % 2 ==0:
        valores[0].append(valor)
    elif valor%2==1:
        valores[1].append(valor)
print("=-"*30)
valores[0].sort()
valores[1].sort()
      
print(valores)
print(f"{valores[1]}")
print(f"{valores[0]}")