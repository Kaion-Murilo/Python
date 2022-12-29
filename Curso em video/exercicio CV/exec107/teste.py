import moeda
p = float(input("digiti o preco: "))
print(f"a metade de {p} e {moeda.metade(p)}")
print(f"O dobro de {p} e {moeda.dobro(p)}")
print(f"Aumento de 1-% temos {p} e {moeda.aumento(p,10)}")