f=str(input("digiti: ")).upper()
print(f.count("A"))
x=list(f)
print(list(f))
e=len(f)
for i in range (e):
    if x[i]=='A':
        h=x[i]
        print("A letra A aparece nas posicao {} ".format(i))
print("A letra A aparece {} vezes na frase.".format(f.count('A')))
print("A primerira letra  A aparecel na posicao {}".format(f.find('A')+1))
print("A primerira letra  A aparecel na posicao {}".format(f.rfind('A')+1))