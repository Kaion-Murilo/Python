import cabesalho
from time import sleep
import arquivo
arq = 'curso.txt'
if arquivo.arquivioExiste(arq):
    print("arquivo encontrado")
else:
    arquivo.criararquivo(arq)
while True:
    resposta=cabesalho.menu(0)
    if resposta == 1:
        print('ver pessoas cadastradas: ')
        arquivo.lerarquivo(arq)
    elif resposta == 2:
        print('leer arquivo')
        cabesalho.cabecalho1('novo cadastro')
        nome=str(input("nome"))
        idade=cabesalho.leiaint('idade: ')
        arquivo.cadastrar(arq,nome,idade,)
    elif resposta == 3:
        print('saiondo do sistema ate llogo ...FIM')
        break
    else:
        sleep(2)
        print('\033[31merros\033[m')