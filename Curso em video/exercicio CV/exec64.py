num = 0
c=0
le=[]
num=int(input("digiti nuvamente:"))
while num!=999:
    c=c+num
    le.append(num)
    num=int(input("digiti nuvamente:"))
print(f"soma{c}")
le.remove(999)
print(f"numeros digitados {le}")
print("FIM")