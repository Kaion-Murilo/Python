from math import hypot
co= float(input("digiti o  cateto oposto: "))
ca= float(input("digiti o  cateto adj: "))
h= hypot(co,ca)
print(" O o valor da hipotenusa de um trangulo de CO {} e CA{} e {:.2f}".format(co,ca,h))
# co= float(input("digiti o  cateto oposto: "))
# ca= float(input("digiti o  cateto adjacente: "))
# h=co**2+ca**2 **(1/2)
# print(" O o valor da hipotes=nusa de um trangulo de CO {} e CA{} e {}".format(co,ca,h))