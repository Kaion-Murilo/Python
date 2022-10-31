sexo = str(input("DIGITI SEU SEXO[F/M]: ")).upper().strip()

while sexo not in  "mfFM":
    print(sexo,"2")
    print("tipo de sexo invalido")
    sexo = str(input("DIGITI SEU SEXO[F/M]: ")).upper().strip()
print(f"sexo {sexo} registrado ")
print("ACABOL")  