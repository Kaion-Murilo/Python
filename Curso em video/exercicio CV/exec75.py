from operator import index


a1=int(input("Digiti o valor:"))
a2=int(input("Digiti o valor:"))
a3=int(input("Digiti o valor:"))
a4=int(input("Digiti o valor:"))
a5=int(input("Digiti o valor:"))
num=(a1,a2,a3,a4,a5)
print(f"O numero 9 aparecel no total de {num.count(9)} vezes")
if num.index(3)>0:
    print(f"O em que posicao aparecel o 3 na posicao {num.index(3)}")
else:
    print(f"O em que posicao aparecel o 3 na posicao {num.index(3)}")
par=[]
for c in range(len(num)):
    v=num[c]%2
    if v==0:
        par.append(num[c])
print(par)