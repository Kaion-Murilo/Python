h=0
l=[]
for c in range (6):
    r=int(input("digiti o {} numero: ".format(c)))
    if  r%2==0:
        h=h+r
print(h)