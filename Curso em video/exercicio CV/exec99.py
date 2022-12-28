from time import sleep
def maior(*num):
    cont=maior=0
    print("-="*30)
    print("Analisabdo os valores ...")
    for valor in num:
        print(f"{valor}",end='',flush=True)
        sleep(0.3)
        if cont == 0:
            maior=valor
        else:
            if valor>maior:
                maior=valor
        cont+=1
    print(f"foram informados {cont} valors ao todo")
    print(f"o maior valor informado foi {maior}")

maior(2,9,4,56,4,48,1)
maior(4,7,0)
maior(2,1)
maior()