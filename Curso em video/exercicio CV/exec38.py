n1=int(input("digiti numero: "))
n2=int(input("digiti numero: "))

if n1>n2:
    print("primeiro {} e maior que o segundo {} ".format(n1,n2))
    
elif n2>n1:
    print("segundo {} e maior que o primeiro {} ".format(n2,n1))

elif n1==n2:
    print("os dois sao iguais {}={}".format(n1,n2))