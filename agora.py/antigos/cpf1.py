import re
class validacpf:
    def __init__(self,cpf):
        self.cpf=cpf
        
        print(f"cpf usado =self.cpf")
        
    def valida(self):
        if not self.cpf:
            return False
        novo_cpf=self._calcula_digito(self.cpf[:9])  
        novo_cpf=self._calcula_digito(novo_cpf)
        if novo_cpf==self.cpf:
            return True
        else:
            return False
    @staticmethod
    
    
    def _calcula_digito(fatia_cpf):
        if not fatia_cpf:
            return False
        sequencia=fatia_cpf[0]*len(fatia_cpf)
        print(sequencia)
        if sequencia == fatia_cpf:
            return False    
        print("ok")
        soma=0
        for chave,multiplicador in enumerate(range(len(fatia_cpf)+1,1,-1)):
            soma += int(fatia_cpf[chave])* multiplicador
            print(soma)
        resto=11-(soma%11)
        resto=resto if resto <=9 else 0
        return fatia_cpf + str(resto)
    @property
    def cpf(self):#1
 
        return self._cpf
    
    @cpf.setter
    def cpf (self,cpf):#2
        self._cpf=self._so_numeros(cpf)
        
           
    @staticmethod
    
    def _so_numeros(cpf):#3
        return re.sub('[^0-9]', '', cpf)
    
cpf=validacpf("529.982.247-25")
"413.717.708-24"
if cpf.valida():
    print("cpf valido")
else:
    print("cpf invalio")