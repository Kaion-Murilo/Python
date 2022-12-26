from operator import index
num=(int(input("Digiti o valor:")),
int(input("Digiti o valor:")),
int(input("Digiti o valor:")),
int(input("Digiti o valor:")),
int(input("Digiti o valor:")))

print(f"O numero 9 aparecel no total de {num.count(9)} vezes")
if 3 in num:
    print(f"O em que posicao aparecel o 3 na posicao {num.index(3)}")
else:
    print(f"O em que posicao aparecel o 3 na posicao em nenhuma")
par=[]
for c in range(len(num)):
    v=num[c]%2
    if v==0:
        par.append(num[c])
print(par)