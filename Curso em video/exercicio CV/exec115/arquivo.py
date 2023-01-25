import cabesalho

def arquivioExiste(nome):
    try:
        a= open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def criararquivo(nome):
    try:
        a= open(nome,'wt+')
        a.close()
    except:
        print("houve um erro na criacao ")
    else:
        print(f"arquivo  {nome} criado")
def lerarquivo(nome):
    try:
        a=open(nome,'rt')
    except:
        print("error ao ler arquivo")
    else:
        cabesalho.cabecalho1("pessoas cadastra das")
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f"{dado[0]:<30}{dado[1]:>3}")
        print(a.read())
    finally:
        a.close()
def cadastrar (arq,nome="desconhecido",idade=0):
    try:
        a=open(arq,'at')
    except:
        print('erro na abertura do arquivo')
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print('houve um erro na hora de escrever')
        else:
            print(f'novo registro de {nome} adicionar,')
            a.close()
