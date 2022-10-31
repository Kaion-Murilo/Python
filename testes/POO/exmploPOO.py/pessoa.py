import datetime
from contracheque import contracheque
class pessoa:
    renda=None
    def __init__(self,nome,sexo,data_nacimento):
        self.nome=nome
        self.sexo=sexo
        self.data_nacimento=data_nacimento
    def get_idade(self):
        idade=int(datetime.datetime.now().year)  
        int(datetime.date.replace(self.data_nacimento).year)
        return idade
    def set_renda(self,valor):
        self.renda=valor