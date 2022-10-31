lanche = ("Hambúrgues","Suco","Pizza","Pudim")
#Tuplas são imutaveis 
print(lanche[:2])
print(lanche[-2])
print(lanche[-2:])
print(lanche[-3:])
for c in lanche:
    print(f"comidas  {c}")
for cont in range(0,len(lanche)):
    print(lanche[c])
for c,p in enumerate(lanche):
    print(f"comidas  {c} na {p}")
    
print(sorted(lanche))
a= (2,3,5,7)
b= (2,3,45,7,9)
c= b + a
print(len(c))
print(c.count(5))
print(c.count(4))
print(c.count(90))
print(c.index(2))
del(a)

