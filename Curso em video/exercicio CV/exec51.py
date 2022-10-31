n1=int(input("DIGITI O TERMO: "))
r=int(input("RAZÃO: "))
dec = n1+(10-1)*r
for i in range(n1,dec+r,r):
    print("{} ".format(i),end="->")
    n2=n1-r
    n1=n2
print('FIM')