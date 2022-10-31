import os
os.system("cls");
'''

lista_vazia = list()
print("Lista vazia", lista_vazia)

lista_pokemon = ['Pikachu', 'Charmander', 'Wobbuffet','Eeve', 'Dragonite']
del lista_pokemon [1]
del lista_pokemon [3]
lista_pokemon.append('Ratata')
print (lista_pokemon)

lista_vazia = []
print("Lista vazia", lista_vazia)

lista_tipos = ["Edjane", 1990, 2.3]
print("Lista de elementos: ", lista_tipos)

lista_inteiros = [3,10,50,40,55]
print ("Lista de inteiros: ", lista_inteiros)


lista=['Kaion','muyilo','mmm']
for i ,p in enumerate (lista):
    print(i+1,'=>',p)
del lista [2]
print(lista)

lista_pokemon = ['Pikachu', 'Charmander', 'Wobbuffet','Eeve', 'Dragonite']
del lista_pokemon [1:3]
print (lista_pokemon)

#copia de listas
a=[1,2,3]
b=a#espelha tudo de [a] 
a.append(4)
print(b)

el=[1,2,3,4,5]
sum(el)#soma de todas as variaveis na  lista 
print(el)

lista=[0,1,2,3,4,5]
lista.insert(1,'tres')
print (lista)

''' 
xy=0 
x= [1,2,3,4,-10]
for i in range (5):
 xy=x[i]+xy
print(xy)