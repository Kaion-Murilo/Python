num = []
while True:
    n = int(input("digiti: "))
    if n not in num:
        num.append(n)
    else:
        print(f"valor ja existente! não vou adicionar...")
        r=str(input("quer continuar?[S/N]"))
    if r in "Nn":
        break
print('-='*30)
print(f"valores digitados {num}")
print(sorted(num))
