num=[]
for t in range(5):
    num.append(int(input("digiti valor: ")))
print(num)
print(f"maior valor {max(num)} posicao :{num.index(max(num))}")
print(f"menor valor {min(num)} posicao :{num.index(min(num))}")