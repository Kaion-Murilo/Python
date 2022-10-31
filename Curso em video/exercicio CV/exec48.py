x=0
cont=0
for c in range(500):
    a=c%2
    b=c%3
    if a==1 and b==0:
        cont=cont+1
        x=x+c
        print(x,end=" ")
        
print(cont)        
print(x)