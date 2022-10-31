# from math import factorial
# x=int(input("digiti seu valor : "))
# f=factorial(x)
# print(f"O valor fatorial de {x} e {f}")
x=int(input("digiti seu valor : "))
f=1
c=x
while c>0:
    print("{} ".format(c),end='')
    print(" x " if c>1 else ' = ',end="")
    f*=c
    c-=1
print("{}".format(f))
