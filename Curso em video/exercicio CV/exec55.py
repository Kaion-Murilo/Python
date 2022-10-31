maior=0
menor=0
for i in range (5):
    x=float(input("digiti: "))
    if i ==1:
        maior = x
        menor = x
    else:
        if x>=maior:
            maior=x
        elif x<=menor:
            menor=x
  
print("O MAIOR PESO LIDO FOI {}Kg ".format(maior))
print("O MENOR PESO LIDO FOI {}Kg ".format(menor))