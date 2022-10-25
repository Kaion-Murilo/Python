from pessoa import pessoa

#heranca - funcionario
class funcionario(pessoa):
    def __init__ (self,cargo,setor,nome,sexo,date_nacimento):
        super(). __init__(nome,sexo,date_nacimento)
        self.cargo=cargo
        self.setor=setor
    def salario(self,horario_extra):
        valor_hora_extra=(self.__salario/30)/8
        total_salario=(horario_extra*valor_hora_extra)+self.__salario
        self.set_renda(total_salario)
        return total_salario
    # def set_renda(self,valor): __annotations__
    def get_setor(self):
        return self