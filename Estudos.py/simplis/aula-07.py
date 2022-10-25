vetor_Inicial = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25,]
'''
print(len(vetor_Inicial))#len retorna quantos elementos possui a estrutura
print(vetor_Inicial[0])
print(vetor_Inicial[1])
print(vetor_Inicial[2])
print(vetor_Inicial[2])
print(vetor_Inicial[3])
print(vetor_Inicial[4])
for i in range(0,8,1):
    print(vetor_Inicial[i])

for i in range(0,len(vetor_Inicial),1):
    print(vetor_Inicial[i])
'''
'''
Qtd_Elem_V=6
vetor = [1]* Qtd_Elem_V

print('\nentre com os valor do vetor:')
for i in range(0,Qtd_Elem_V,1):
    print(f'infomee o elemenross da posiçao{i+1}:')
    vetor[i]=float(input())

print(vetor) 


Qtd_Elem_V=6
A=[1]*Qtd_Elem_V
vet_A= [1,0,5,-2,-5]
#vet_A= [1,0,5,-2,-5,7]
print('\nentre com o valor do vertor:')
for i in  range (0,Qtd_Elem_V,1):
 A [i]=int(input(f'informe o valor da posiçao {i+1}: '))
print(A)
soma=A[0]+A[1]+A[5]
print(soma)
A[4]=100
print(A)
print(f'\nsoma= {soma}\n')
for i in  range(0,Qtd_Elem_V,1):
  print (f'posiçao {i+1} ={A[i]}\n')
'''

matriz=[[166,2004,3],
       [4,555,655],
       [7444,8,9544]]
print(matriz)
for i in range (0,len(matriz),1):
    print(matriz[i])
   
for l in range (0,len(matriz),1):
    for c in range (0,len(matriz),1):
        print(f'[{matriz [l][c]:^5}]',end='-')
    print()
    