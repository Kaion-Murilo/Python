peso=float(input("digiti peso:(kg) "))
altura=float(input("digiti altura:(m) "))

imc=peso/(altura*altura)
print("O IMC dessa pessoa e de {:.1f}".format(imc))
if imc<18.5:
    print("abaixo do peso")
elif 18.5<=imc<= 25:
    print(" peso ideal")
elif 25<= imc <30 :
    print("spbre peso")
elif 30<= imc <40:
    print("obesidade")
elif imc>40:
    print("obesidade morbida")