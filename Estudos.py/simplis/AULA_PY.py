
lista1 = []
lista2 = [0,1,2,3,4,5,56,6,7,8,9,10,11,12,7,90]
lista3 = ['N','a','t','a','l',' ','c','i','d','a','d','e',' ','d','o',' ','S','o','l']
lista4 = list('Universidade Potiguar')
lista5 = list(range(11))

#Memórias
'''
# Lista código ASCII dos itens da lista
lista = ['a','b','c','d','A','B','C','D',' ']
num=[]
for i in lista:
    num.append(ord(i))

print(num)

# Adicionar um elemento na lista com append()
num = []
for i in range(0, 5):
    num.append(int(input('Informe um número: ')))

print(num)

num.append([23,45])
print(num)


# Adicionar mais de um elemento na lista com extend()
num.extend([99,88,77])
print(num)


# Exclusão da lista com pop()
print(lista2.pop())
print(lista2)
print(lista2.pop(3))
print(lista2)


# Classificando listas com sort()
lista2.sort()
print(lista2)

# Inverte a ordem da lista com reverse()
lista2.reverse()
print(lista2)

# Contagem de ocorrência dentro da lista count()
print(lista2.count(7))

# Conversão de String em Lista com split()
curso = 'Ciência da Computação'
#curso = 'Ciência,da,Computação'
curso = curso.split()
print(curso)
# Conversão de Lista em String com join()
curso = ' '.join(curso)
print(curso)


# Iteração de listas com FOR
soma = ' ' # Se for iterar em uma lista numérica, o valor de soma deve ser 0
for i in lista3:
    print(i)
    soma += i

print(soma)

# Iteração com While
carrinho = []
produto = ''

while produto != 'sair':
    print('Adicione produto no carrinho (Digite "sair" par sair) :')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

carrinho.sort()
print(carrinho) 

# Acesso indexado aos itens da lista
cores = ['branco', 'azul', 'amarelo', 'verde', 'vermelho']
print(cores)

for cor in cores:
    print(cor)

indice = 0

while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

# Encontrar o índice dos elementos com index()
print(lista2.index(90))
print(lista2.index(56, 4, 8))
'''
# Usando o Slice
print(lista2[:])
print(lista2[3:])
print(lista2[3:7])
'''


# Listas básicas

print(lista4)
print(lista5)
'''