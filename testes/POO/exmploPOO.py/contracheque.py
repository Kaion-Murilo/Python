
class contracheque:
    total_salario=None
    custovalealimentacao=548.00
    salario_funcionario = 2000
    def imprimir_contracheque(self):
        self.salario_funcionario =self.funcionario.Salario(50)
          
    def __init__(self,funcionario,passe_vale_alimentacao):
        self.funcionario=funcionario
        self.passe_vale_alimentacao=passe_vale_alimentacao
        if self.passe_vale_alimentacao:
            self.total_salario= self.salario_funcionario + self.custovalealimentaca
        else:
            self.total_salario=self.salario_funcionario
    
        folha_pagemento="""nome:{}
                       cargo:{}    
                       setor:{}
                       salario:{}""".format(self.funcionario.nome,self.funcionario.cargo,set.funcionario.get_setor(),self.total_Salario)
        return folha_pagemento
                         