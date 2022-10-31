class Pessoa:
    def __init__(self,nome,idade):
        self.idade=idade
        self.nome=nome
    @property    
    def nome(self):
        return self.nome
    @property
    def idade(self):
        return self.idade

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome,idade)
        self.conta=None
        
    def inserir_conta(self,conta):
        self.conta=conta
    
    def inprimirvalores(self):
        print(self.nome)
        print(self.idade)
        print(self.conta)
    