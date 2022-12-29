from time import sleep
c=('\033[m' # 0 sem cores
    '\033[0;30;41m' # 1 vermelho
    '\033[0;30;42m' # 2 - verde
    '\033[0;30;43m' # 3- amarele
    '\033[0;30;44m' # 4 azul
    '\033[0;30;45m' # 5 roxo
    '\033[7;30m' # 6 branco
            );
def ajuda(com):
    titulo(f'acessando o manual de comando\'{com}\'',4)
    print(c[6],end='')
    help(com)
    print(c[0],end='')
    sleep(2)
def titulo(msg,cor = 0):
    tam=len(msg)+4
    print(c[cor],end='')
    print("~"*tam)
    print(f'  {msg}  ')
    print("~"*tam)
    print(c[0],end='')
    sleep(1)
comamdo=''
while True:
    titulo('sistema de ajuda pyhelp',2)
    comamdo=str(input(f'fincao ou biblioteca'))
    if comamdo.upper() =='FIM':
        break
    else:
        ajuda(comamdo)
titulo('ate logo',1)