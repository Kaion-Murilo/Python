matrix=[[1,2,3],[4,5,6],[7,8,9]]

print(matrix)
for i in range (0,3):
    for e in range (0,3):
        matrix[i][e]=int (input(f"digiti o valor que ficarar na posicao [{i}/{e}]: "))
print("-="*30)
for i in range (0,3):
    for e in range (0,3):
       print(f"[{matrix[i][e]:^5}] ",end='')
    print()