import cliente
class Banco:
    def __init__(self):
        self.agencia=[123,231,312]
        self.clientes=[]
        self.conta=[]
        
    def inserir_cliente(self,cliente):
        self.clientes.append(cliente)
        
    def inserir_conta(self,conta):
        self.conta.append(conta)
    
    def autenticar(self,cliente):
        if cliente in self.clientes:
            return True
        if cliente.conta in self.conta:
            return True
        if cliente.conta in self.agencia:
            return True
        return False