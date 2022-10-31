
from turtle import pen


valor=float(input("   digiti o valor da casa:  "))
salario=float(input("     digiti seu salario:    "))
parcalas=float(input("   digiti quantos anos:  "))
me=valor / (parcalas*12)
print(me)
con=salario*30/100
print("para pagar uma  casa de R${:.2f} em {} ".format(valor,parcalas), end="")
print("O prestacao sera begada de R$ {:.2f}".format(me))
if con<=me:
    print("nao e posivel realizar conpra ")
else:
    print("conpra aprovada{}{}")
