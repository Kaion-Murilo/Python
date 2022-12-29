import moeda


p = float(input("digiti o preco: "))
print(f"a metade de {moeda.moeda(p,'US$')} e {moeda.moeda(moeda.metade(p))}")
print(f"O dobro de {moeda.moeda(p)} e {moeda.moeda(moeda.dobro(p))}")
print(f"Aumento de 1-% temos e {moeda.moeda(moeda.aumento(p,10))}")