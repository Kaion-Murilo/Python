def leiaint(msg):
    ok=False
    valor= 0
    while True:
        n=str(input(msg))
        if n.isnumeric():
            valor=int(n)
            ok=True
        else:
            print('\033[0;31mErro digiti um numero.\033[m')
        if ok:
            break
    return valor
n=leiaint("digiti um numero")
print(f"voce acabou de digitar o numero {n}")