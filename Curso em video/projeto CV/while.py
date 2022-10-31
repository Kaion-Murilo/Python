"""r = 's'
for c in range (1,5):
    n=int(input("digiti"))
while r == 's':
    n = int(input('digiti um valor: '))
    n = str(input('queer conyinuar ?[s/n]: '))
print("FIM")"""
from asyncio import shield


n=1
par = impar =0
while n != 0:
    n= int(input("digiti")) 
    if n !=0:
        if n%2==0:
            par+=1
        else:
            impar+=1
print(f"voçê digitol {par} numeros pares e {impar} numeros impares")