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
def linha(tam=42):
    return '-'*tam
def cabecalho1 (txt):
    print(linha())
    print(txt.center(42))
    print(linha())
def menu(lista):
    cabecalho1('sistema teste de arquivo')
    c = 1
    lista=['criar arquivo','cadastrar pessoa','lista de pessoas']
    for item in lista:
        print(f"\033[33m{c}\033[m - \033[34m{item}\033[m")
        c+=1
    print(linha())
    opc= leiaint("\033[32msua opicao \033[m")
    return opc