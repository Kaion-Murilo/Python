n1=float(input("digiti sua  nota :"))
n2=float(input("digiti sua  nota :"))
notaf=(n1+n2)/2
if notaf>=7:
    print("aprovado")
elif notaf<=5:
    print("reprovado")
elif notaf>5 and notaf<6.9:
    print("recuperacao")
