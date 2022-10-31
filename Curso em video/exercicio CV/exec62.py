from time import sleep
n2=0
pri=int(input("DIGITI O TERMO: "))
r=int(input("RAZÃO: "))
termo=pri
cont=1
total=0
mais=10
while mais !=0 :
    total =total+mais
    while cont <=total:
        print("{} -> ".format(termo),end="->")
        termo += r
        cont += 1
    print('Pausa')
    mais = int(input("quantos  termps voce quer mostrar agora :"))
print("progressao finalizada com {} termos mostrado".format(total))
print('FIM')