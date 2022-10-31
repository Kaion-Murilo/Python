


cpf_numerado=[]

def numerarcpf():
    for a in cpf:
        a=int(a)
        cpf_numerado.append(a)

def quantidade():
    if len(cpf)<11 or len(cpf)>11:
            print("erro,quantidade")
            return False
    else:
            print("passou,quantidade")
        
            return True
def primeiro_digito():   
    if len(cpf_numerado)<11 or len(cpf_numerado)>11:
        return False
    else:
        acumulador=0
        resultado=0
        controlador=10
        for numeros in cpf_numerado[0:9]:
            resultado=numeros*controlador
            acumulador+=resultado
            controlador=controlador-1
        acumulador=acumulador*10 % 11        
    if acumulador == 10:
        acumulador = 0
    if acumulador == cpf_numerado[9]:
                print("pasou,primeiro digito")
                return True
    else:
                print("erro,primeiro digito")
                return False
                
def segundo_digito():
    if len(cpf_numerado)<11 or len(cpf_numerado)>11:
            return False
    else:
        acumulador2=0
        resultado2=0    
        controlador2=11
        for numeros2 in cpf_numerado[0:10]:
                resultado2=numeros2*controlador2
                acumulador2+=resultado2
                controlador2=controlador2-1
        acumulador2=acumulador2*10%11
        if acumulador2 == 10:
            acumulador2=0
        if acumulador2 == cpf_numerado[10]:
            print("segundo_digito pasou")
            return True
        else:
            print("segundo_digito nao exec") 
            return False
def finalcpf():
    if quantidade() == True and primeiro_digito() == True and segundo_digito() == True:
            print(f"o cpf valido:")  
    else:
            print(f"invalido  :") 


        
# cpf_numerado=[]
cpf=str(input("cpf:  ")).replace('.', '').replace('-', '')
numerarcpf()
print(cpf_numerado)
quantidade()
primeiro_digito()
segundo_digito()
finalcpf()



def validaridade(idade):
        if idade>100 or idade<0:
           return False
        else:
            print("idade validada")
            return True
def validardinheiro(dinheiro):
        dinheiro
        if dinheiro<0 :
            print("dinheiro invalida")
        else:
            print("dinheiro validada")