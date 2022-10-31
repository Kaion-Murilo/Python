print('-=-'*20)
x=float(input("digiti distancia: "))
print("Voce esta preste a comecar a uma viagen de {}KM".format(x))
if x>200:
    preco=x*0.45
    print("valor aciama de 200 Km a ser pago:{}".format(preco))
    
else:
    preco=x*0.5
    print("valor abaixo de 200 a ser pago:{}".format(preco))