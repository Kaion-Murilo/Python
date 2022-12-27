teste=list()
teste.append("gustavo")
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = "Maria"
teste[1] = 22
galera.append(teste[:])
print(galera)
G=[["joao",19],["ana",33],["joaquin",13],['maria',45]]
for p  in G:
    print(f"{p[0]} tem {p[1]} anos")
ga= list()
dado=list
for c in range(0,3):
    dado.append(str(input("name: ")))
    dado.append(int(input("IDADE: ")))
    ga.append(dado[:])
    dado.clear()
print(galera)
for p in ga:
    if p[1]>=21:
        print(f"{p[0]} e maior de idae")
    else:
        print(f"{p[0]} e MENOR de idae")