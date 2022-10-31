v = str(input("digiti o numero"))
print("total de unidedades e de {}".format ( v[3]))
print("na casa das dezenas e de {}".format ( v[2]))
print("na casa das centena e de {}".format ( v[1]))
print("na casa das milhar e de  {}".format ( v[0]))
f = int(input("digiti o numero"))
u = f//1%10
d = f // 10%10
c = f // 100 % 10
m = f // 1000 % 10
print("total de unidedades e de {}".format( u ))
print("na casa das dezenas e de {}".format(d))
print("na casa das centena e de {}".format(c))
print("na casa das milhar e de {}".format(m))