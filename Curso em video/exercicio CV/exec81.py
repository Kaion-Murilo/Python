valores= []
while True:
    valores.append( int(input("digiti: ")))
    r=str(input("quer continuar?[S/N]"))
    if r in "Nn":
        break
print('=-'*30)
print(f"voce digitou {len(valores)} elementos")
valores.sort(reverse=True)
print(f"os valores digitados em orden decrecente sao {valores}")
if 5 in valores:
    print("o valor 5 faz parte da lista")
else:
    print("o valor 5 nao faz parte da lista") 