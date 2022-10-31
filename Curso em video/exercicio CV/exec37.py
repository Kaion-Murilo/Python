print("-=-"*20)
num=int(input("qual valor deseja converter:  "))
de=int(input("""digiti sua escolha\n1=binario\n2=octal \n3=hexadecimal \ndigiti sua escolha:  """))
print("-=-"*20, "\n")
if de==1:
    print("O numero {} em  Binario á: {} ".format(num,bin(num)[2:]))
elif de==2:
    print("O o numero {}   em octal á: {} ".format(num,oct(num)[2:]))
elif de==3:
    print("O numero   {}  em hexademal á: {} ".format(num,hex(num)[2:]))
else:
    print("opcao invalida")
print("-=-"*20)
