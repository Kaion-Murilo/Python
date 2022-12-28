aluno = dict()
aluno["nome"]=str(input("Nome: "))
aluno["media"]=float(input(f"media de {aluno['nome']}; "))
if aluno["media"]>=7:
    aluno["situacao "] = "aprovado"
elif 5 <= aluno["media"]<7:
    aluno["situacao "]="recuperacao"
else:
    aluno["situacao "]="reprovado"
print("-="*30)
for k,v in aluno.items():
    print(f"-{k}e iguall a {v}")