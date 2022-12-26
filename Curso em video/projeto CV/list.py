num=[2,3,4,5,6,8,9,90,22,44,4,5,7,98,33,22,]
num[2]=4
num.append(7)
num.sort()
num.sort(reverse=True)
num.insert(2,0)
print(num)
num.remove(2)
if 5 in num:
    num.remove(5)
else:
    print("nao achei")

valorers = []
for c in range(5):
    valorers=int(input("digiti um valor"))
for c,v in enumerate(valorers):
    print(f"na posicao {c} rncontrei o valor {v}")
print("FIM")
v=[1,23,4,65,7]
f=v[:]