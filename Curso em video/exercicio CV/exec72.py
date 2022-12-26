extenso=("Zero","Um","dois","Tres", "quatro", "cinco", "seis", "sete" ,"oito" ,"nove" ,"dez" ,"onze", "doze", "treze", "catose" ,"quinze", "dezesseis", "dezesete" ,"dezoito", "ddesenove" ,"vinte")
num = int(input("digiti o numero:"))
while num > 20 or num<0:
    print("por favor digiti um numero valido")
    num = int(input("digiti o numero:"))
print(f"o numero por extenso de {num } e {extenso[num]}")
y=input("se desejar sair e so digitar S: ",)
if y =="S":
    StopAsyncIteration
    