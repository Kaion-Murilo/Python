num = []
while True:
    x=int(input("digiti: "))
    print(num.count(x))
    if num.count(x)>0:
        print("valor existente")
    else:
        int(x)
        num.append(x)
    y=str(input("deseja continuar C ou sair=S"))
    if y=="S":
        break
print(sorted(num))
