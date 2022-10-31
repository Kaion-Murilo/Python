from datetime import date
atual=date.today().year
nac=int(input("digiti sua data de nacimento"))
idade = atual - nac
print("O atleta tem {}".format(idade))
if idade <= 9:
    print("mirim")
elif idade<=14:
    print("infantil")
elif  idade<19:
    print("junior")
elif idade<=20:
    print("senio")
elif idade>20:
    print("master")