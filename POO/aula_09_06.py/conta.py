from abc import ABC,abstractclassmethod
class Conta(ABC):
    def __init__(self,agencia,conta,saldo):
        self.conta=conta
        self.agencia=agencia
        self.saldo=saldo
    def deposito(self,valor):
        self.saldo+=valor
        self.detalhes()
        
    def detalhes(self):
        print(f"agencia:{self.agencia}"
              "conta:{self.conta}"
              "seldo{self.saldo}"
              "oi")
    @abstractclassmethod
    def sacar(self,valor):pass

class ContaPoupanca(Conta):
    def sacar(self,valor):
        if self.saldo<valor:
            print("tem nao ,hein")
            return
        self.saldo-=valor
class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo,limiti=100):
        super.__init__(agencia,saldo,conta)
        self.limiti=limiti
    def sacar(self,valor):
        if (self.saldo+self.limiti)<valor:
            print("saldo insurficiente")
            return
        self.saldo-=valor
        self.detalhes()   