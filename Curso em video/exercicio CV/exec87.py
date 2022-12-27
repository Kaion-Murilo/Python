matrix=[[1,2,3],[4,5,6],[7,8,9]]
spar=mai=scol=0
for i in range (0,3):
    for e in range (0,3):
        matrix[i][e]=int (input(f"digiti o valor que ficarar na posicao [{i}/{e}]: "))
print("-="*30)
for i in range (0,3):
    for e in range (0,3):
        print(f"[{matrix[i][e]:^5}] ",end='')
        if matrix[i][e] % 2 == 0:
            spar+= matrix[i][e]
    print()
print("=-"*30)
print(f"A soma de valores pares e {spar}")
for l in range(0,3):
    scol+= matrix[i][2]
print(f"A soma dos valors da 2 coluna e {scol}.")
for c in range(0,3):
    if  c==0:
        mai=matrix[1][c]
    elif matrix[1][c] >mai:
        mai=matrix[1][c]
print(f"O maior valor da segunda linha e {mai}")