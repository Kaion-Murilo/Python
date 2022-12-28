from time import sleep


def contador(i,f,p):
    if p<0:
        p *= -1
    if p== 0 :
        p=1
    print("-="*20)
    print(f"contagen de {i} ate {f} de  {p} em {p}")
    sleep(2.5)
    if i<f :
        cont=i
        while cont <= f :
            print(f'{cont}',end="",flush=True)
            sleep(0.5)
            cont += p
        print("Fim")
    else:
        cont= i
        while cont >=f:
            print(f"{cont} ",end="",flush=True)
            sleep(0.5)
            cont -=p
        print(  "fIM")
contador(1,10,1)
contador(10,0,2)
print('=-'*20)
print("agora e sua vez pessoanaliza a contagen")
ini = int(input("inicio: "))
fim = int(input("fim: "))
pas = int(input("passo: "))
contador(ini,fim,pas)