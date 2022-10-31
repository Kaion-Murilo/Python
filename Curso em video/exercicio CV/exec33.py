from statistics import mean


v=[]
n1=int(input("digiti :"))
v.append(n1)
n2=int(input("digiti :"))
v.append(n2)
n3=int(input("digiti :"))
v.append(n3)
v.sort()
print("O  primeiro e {}".format(v[0]))
print("o ultomo e {}".format(v[2]))
menor=n1
if n2<n1 and n2<n3:
    menor= n2
if n3<n1 and n3<n2:
    menor=n3   
maior=n1
if n2>n1 and n2>n3:
    maior= n2
if n3>n1 and n3>n2:
    maior=n3