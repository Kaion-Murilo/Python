p=3
s=0
c=0
while resp in "Ss":
    num=int(input("digiti: "))
    c=c+1
    s=s+num
    if c==0:
        maior=num
        menor=num
    else:
        if num>maior:
            maior=num
        elif num<=menor:
            menor=num
    resp=str(input("digiti se se deseja continuar"))
print(f"maior valor {maior} menor valor {menor}")
print(f"media de tudo foi  {s/c:.2f}")