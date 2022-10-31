
x=str(input("ddigiti: ")).upper().strip()
frase=x.split()
juncao= ''.join(x)
inv = ""
for v in range(len(juncao)-1,-1,-1):
    inv += juncao[v]
        
if inv==juncao:
    print("temos um palindromo")
else:
    print("não e ")