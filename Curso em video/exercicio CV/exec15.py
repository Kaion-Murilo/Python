d=float(input("quantos dias voce ficol com o carro: "))
k=float(input("quantos KM rodados :"))
p1=d* 60
p2=k* 0.15
print("O carro teve {} dias alugados e {}KM rodados entao o valor a ser pago e {}".format(d,k,(p1+p2)))