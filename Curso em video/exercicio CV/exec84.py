dado=list()
pessoas=[]
men=mai=0
while True:
        dado.append(str(input("name: ")))
        dado.append(float(input("Peso: ")))
        pessoas.append(dado[:])
        if len(pessoas)==0:
            mai=men=dado[1]
            if dado[1]>mai:
                mai=dado[1]
            if dado[1]<men:
                men=dado[1]
        resp=str(input("deseja continuar?[s/n]"))
        if resp in "Nn":
            break
        dado.clear()
print("=-"*30)
print(f"numero de pessoas cadastradas {len(pessoas)}")
print(f"O maior peso foi de {mai} .peso de  ",end="")
for i in range(len(pessoas)):
    if pessoas[i][1]==mai:
        print(f"{pessoas[i][0]}...",end="")
print()
print(f"O menor peso foi de {men} .peso de  ",end="")
for i in range(len(pessoas)):    
    if pessoas[i][1]==mai:
        print(f"{pessoas[i][0]}...",end="")
