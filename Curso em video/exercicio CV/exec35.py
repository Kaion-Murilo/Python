# |10 – 9| < 5 < 10 + 9
# 1 < 5 <19 (VERDADEIRO)

# |9 – 5| < 10 < 9 + 5
# 4 < 10 < 14 (VERDADEIRO)

# |5 – 10| < 9 < 10 + 5
# 5 < 9 < 15 (VERDADEIRO)
print("-=-"*20)
r1=int(input("digiti: "))
r2=int(input("digiti: "))
r3=int(input("digiti: "))
print("-=-"*20)

if (r2-r3)<r1<(r2+r3) and (r1-r3)<r2<(r1+r3) and (r2-r1)<r3<(r2+r1) :
    print("     pode formar um triangulo         ")
else:
    print("     NAO pode formar um triangulo     ")
print("-=-"*20)
    