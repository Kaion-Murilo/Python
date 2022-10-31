from time import sleep

o=6
n1=int(input("digiyi seu primeiro numero: "))
n2=int(input("digiyi seu segundo numero: "))
while o!=0:
    o=int(input("digiti sua escolha \nsoma=1\nmultiplicacao=2\nmaior=3\nnovos numeros=4:\nsair=0"))
    if o == 1:
        print(f"A soma dos valor {n1}+{n2}={n1+n2}")
        sleep(2)
    elif o == 2:
        print(f"A mult dos valor {n1}X{n2}={n1*n2}")
        sleep(2)
    elif o == 3:
        if n1>n2:
            print(f"entre {n1} e {n2}o maior valor e {n1}")
            sleep(2)
        else :
            print(f"entre os valores {n1} e {n2}o maior valor e {n2}")
            sleep(2)
    elif o==4:
        n1=int(input(f"digiyi seu primeiro numero"))
        n2=int(input(f"digiyi seu segundo numero"))
        sleep(2)
    else:
        print("opcao invalida")
print("FIM")
    