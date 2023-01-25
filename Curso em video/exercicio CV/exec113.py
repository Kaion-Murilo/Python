def leiaint(msg):
    while True:
        try:
            n=int(input(msg))
        except(ValueError,TypeError):
            print("\033[31m ERRO por favor \033[m")
            continue
        except(KeyboardInterrupt):
            print("\n\033[31m Usuario preferiu nao digitar.\033[m")
            return 0
        else:
            return n
def leiafloat(msg):
    while True:
        try:
            n=float(input(msg))
        except(ValueError,TypeError):
            print("\033[31m ERRO por favor \033[m")
            continue
        except(KeyboardInterrupt):
            print("\n\033[31m Usuario preferiu nao digitar.\033[m")
            return 0
        else:
            return n
n1 = leiaint("digiti um inteito :  ")
n2 = leiafloat("digiti um real :  ")
print(f"valor digitado foi {n1} e real foi {n2}")