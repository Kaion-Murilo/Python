print('-=-'*20)
velocidade=float(input("digiti sua velocidade : "))
print('-=-'*20)
if velocidade>80:
    diferenca=velocidade-80
    valor=diferenca*7
    print("voce foi multado, é a multa vai custar {:.2f} reais ".format(valor))
else:
    print("voce não foi multado ")
print("   Dirija com cuidado   ")
print('-=-'*20)
