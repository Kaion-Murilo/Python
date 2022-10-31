import os 
os.system('cls')
li=[]
aluw=[]
h=0
arquivo=open('tx.txt','w')
while h!=2:
    h=int(input("digitio o que quer"))
    if h==1 :
     nome=str(input('nome d aluno'))
     ema=str(input('ema d aluno'))
     curso=str(input('curso d aluno'))
     aluw.extend([nome,ema,curso])
     li.append(nome)
     li.append(ema)
     li.append(curso)
     arquivo=open('tx.txt','w')
     arquivo.write(str(li[0]) +'; ')
     arquivo.write(str(li[1]) +'; ')
     arquivo.write(str(curso[2]) +'; ') 
     print(aluw)
    elif 2 ==h:
        arquivo=open('tx.txt','r')
        conteudo=arquivo.read()
       
        print(conteudo)
        arquivo.close()
else:
     if 3== h:
         bus=str(input("digiti a busca"))
         print(aluw.index(bus))
         vc=int(input("voce dewseja o excluir"))
     if 4==h:
         k=int(input('digiti a posicao'))
         print(aluw.pop(k))


    