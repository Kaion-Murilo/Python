ficha = list()
while True:
    name=str(input("nome: "))
    nota1=float(input("nota1: "))
    nota2=float(input("nota2: "))
    media=(nota1+nota2)/2
    ficha.append([name,[nota1,nota2],media])
    resp=str(input('quer continuar?[S/N]'))
    if resp in "Nn":
        break
print("=-"*30)
print(f'{"NO.":<4}{"nome":<10}{"media":>8}')
print("-"*26)
for i,a in enumerate(ficha):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")
while True:
    print("-"*30)
    opc=int(input("nostrar notas de qual aluno? (999 interronpe)"))
    if opc==999:
        print("finalizar...")
        break
    if opc<=len(ficha)-1:
        print(f"notas de {ficha[opc][0]} sao {ficha[opc][1]}")
print("<<<<Volte Sempre>>>.")