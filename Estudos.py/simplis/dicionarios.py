
import os
os.system("cls");
'''
dic={'titulo':'stae war','ano':1234,'diretor':'geor miler'}
print(dic['titulo'])

print(dic.keys())
print(dic.values())
print(dic.items())
-------------------------------------------------------------------
for k,v in dic.items():
    print(f"{k}  =  {v}")
    
del dic['ano']
dic["titulo"]='leandro'
dic['peso']=908
print (dic)
-------------------------------------------------------------------
brasil=[]
estado1={'uf':'rio de janeiro','sigla':'rj'}
estado2={'uf':'sao paulo','sigla':'sp'}

brasil.append(estado1)
brasil.append(estado2)
print(brasil[0])
print(brasil[1])
print(brasil[0]['sigla']) 
print(brasil[1]['sigla']) 
'''
estado={}
brasil=[]
for i in range (3):
    estado['nome']=input("escreva nomr")
    estado['sigla']=input("escreva sglr")
    brasil.append(estado.copy())#memas coisa de [:]
print(brasil)
for e in brasil:
    for k , v in e.items():
        print(f"{k} == {v}")