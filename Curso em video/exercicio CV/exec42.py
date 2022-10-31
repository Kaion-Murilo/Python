print("-=-"*20)
r1=int(input("digiti: "))
r2=int(input("digiti: "))
r3=int(input("digiti: "))
print("-=-"*20)

if (r2-r3)<r1<(r2+r3) and (r1-r3)<r2<(r1+r3) and (r2-r1)<r3<(r2+r1) :
    print("     pode formar um triangulo         ")
    if r1==r2==r3 :
        print("triangulo equilatero")
    elif r1==r2 or r1==r2 or r3==r2 :
        print("triangulo isoceles")
    elif  r1!=r2!=r3!=r1:
        print("triangulo escaleno")
else:
    print("     NAO pode formar um triangulo     ")
print("-=-"*20)


print("fim")