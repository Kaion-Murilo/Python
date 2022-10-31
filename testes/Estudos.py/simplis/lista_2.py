
import os
os.system("cls");
'''
x=0
y=0
h=0
a=int(input("digiti"))
b=int(input("digiti"))
c=int(input("digiti"))
d=int(input("digiti"))
x=a-c
y=b-d
h=x+y
num=h
raiz = float(num) ** 0.5
print(f'\nA raiz quadrada de {num} é {raiz}\n')

a=int(input("digiti"))
b=int(input("digiti"))
c=int(input("digiti"))
x=a+b
y=c+b
s=x*x
r=y*y
z=r+s
d=z/2
print(d)

d=int(input('dia'))
m=int(input('mes'))
a=int(input('dan'))
x=m*30
y=a*365
h=x+y+d
print('dias',h)

d=float(input('dia'))
a=d/360
d=d%360
m=d/30
d=d%30

print('dias',d)
print('mes',m)
print('ano',a)

s=float(input('dia'))
h=s/360
s=s%360
m=s%30
s=s%30

print('dias',s)
print('mes',m)
print('ano',h)
'''

vt=it=v=j=v=i=int
v=int(input("digiti o valor do carro"))
i=v+(v*28/100)
print(i)
j=v+(v*46/100)
print(j)
vt=v+j+i
print("valoe",vt)