
from random import randint
acu=0
dec=False
v=0
while True:
    comp=randint(1,10)
    mao=int (input("ddigiti valor : "))
    tipo=' '
    
    while tipo not in" PIip":
        tipo=str(input("digiti forma [1=par] e [2 = impar]")).upper().strip()
    
    print(f" Rsltado voce jogol {mao} e comp {comp}")
    print(f"DEu par "if (comp+mao) % 2==0 else "DEu inmpar")
    if tipo==1:
        r=(comp+mao)%2
        if r==0:
            print("vitoria do jogaddor")
            acu+=1
        else:
            print("voce perdeu")
            break
    elif tipo==2:
        r=(comp+mao)%2
        if r!=0:
            acu+=1
            print("vitoria do jogaddor")
        else:
            print("voce perdeu")
            break    
    print(f" Rsltado voce jogol {mao} e comp {comp}")

print(f" Rsltado voce jogol {mao} e comp {comp}")
print(f"vitorias consecutivas {acu} ")
