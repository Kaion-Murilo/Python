x=0
tot=0
x=int(input("DIGITI UM NUMERO: "))
for v in range(1,x+1,1):
    if x%v==0:
        print(f"\033[33m",end=' ')
        tot +=1
    else:
        print("\033[31m",end=' ')
    print(f"{v}",end=" ")
print("\n\033[mO numero {} foi divisivel {} vezes".format(x,tot))
print("\033[m")
if tot==2:
    print("E por isso ele e  PRIMO")
else:
    print('por isso ele não e primo')
