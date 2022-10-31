from time import sleep
n2=0
pri=int(input("DIGITI O TERMO: "))
r=int(input("RAZÃO: "))
termo=pri
cont=1
while cont <= 10:
    print("{} ".format(termo),end="->")
    termo += r
    cont += 1
print('FIM')