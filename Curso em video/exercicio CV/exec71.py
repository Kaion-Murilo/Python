# from math import trunc
# cinc=0
# num= int(input("digiti valor a seer sacado: "))
# n1=num / 50
# cinc=(trunc(n1))
# num=num-(cinc*50)
# n1=num / 20
# vin=(trunc(n1))
# num=num-(vin*20)
# n1=num / 10
# dec=(trunc(n1))
# num=num-(dec*10)
# um=num
# print(f'50 { cinc} 20 {vin} 10 {dec} 1 {um}')
print("="*20)
print("{:.30".format("BANCO KAION"))
print("="*20)
valor = int (input("Qual valor voce quer sacar:"))
total =valor
ced = 50 
totalced=0
while True:
    if total >= ced:
        total-=ced
        totalced+=1
    else:
        if totalced>0:
            print(f'Total de {totalced} ceduls de R${ced}')
        if ced==50:
            ced=20
        elif ced == 20:
            ced=10
        elif ced==10:
            ced= 1
        totalced=0
        if total==0:
            break
print("="*20)
print("VOLTE SEMPRE <3")