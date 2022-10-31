print('{:=^40}'.format("loginha do Bairro"))
preco=float(input("digiti preco: "))
opcao=float(input('''digiti forma 
1=dinheiro:
2=2x cartao:
3= 2x cartao: 
4= 3x ou mais cartao: 
digiti forma:  '''))
if opcao==1:
    total=preco-(preco*10/100)
    print("Sua compra de {}  o valor a ser pago {}" .format(preco,total))
elif opcao==2:
    total=preco-(preco*5/100)
    print("Sua compra de {}  o valor a ser pago sera {}" .format(preco,total))
elif opcao==3:
    total=preco
    parcela = total/2
    total=preco+(preco*20/100)
    print("sua compra sera parcelada em duas vezes de R${}" .format(parcela))
elif opcao==4:
    total=preco+(preco*20/100)
    totalp= int(input("quantas parcelas:  "))
    parcela=total/totalp
    print("sua compra sera parcelada em {} vezes de R${}" .format(totalp,parcela))
else:
    print("opcao invalida")
print("sua compra de R$ {:.2f}Vai custar R${:.2f} no final ".format(preco,total))