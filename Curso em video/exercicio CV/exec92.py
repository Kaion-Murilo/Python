from datetime import datetime
dado= dict()
dado["nome"]= str(input("nome: "))
nesc = int(input("ano de nacimento:  "))
dado["idade"]= datetime.now().year- nesc
dado["ctps"] = int(input("carteira de trabelho (0 nao tem)"))
if dado["ctps"]!= 0 :
    dado['contratacao'] = int(input("ano de contratacao"))
    dado['salario'] = float(input("salario:  "))
    dado["aposentadoria"] = dado["idade"]+((dado["contratacao"]+35)- datetime.now().year)
print("=-"*30)
for k,v in dado.items():
    print(f"  - {k} tem o valor {v}")