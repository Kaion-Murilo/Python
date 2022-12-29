import moeda


p = float(input("digiti o preco: "))
print(f"a metade de {moeda.moeda(p)} e {moeda.metade(p,True)}")
print(f"O dobro de {moeda.moeda(p)} e {moeda.dobro(p,True)}")
print(f"Aumento de 10% temos e {moeda.aumento(p,10,True)}")
print(f"Aumento de 13% temos e {moeda.diminuir(p,13,True)}")