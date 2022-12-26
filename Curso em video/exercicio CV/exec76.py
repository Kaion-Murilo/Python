lista=("lapis",1.45,"borracah",2,"caderno",19.9,"estojo",25,"trasferidor",4.23,"compasso",9.99,"mochila",120.32,"caneta",22.30,"livor",34.90)
print("-"*40)
print("listagen de precos")
print("-"*40)
for pos in range(0,len(lista)):
    if pos %2==0:
        print(f"{lista[pos]:.<30}",end="") 
    else:
        print(f"R${lista[pos]:>7.2f}")
print("-"*40)