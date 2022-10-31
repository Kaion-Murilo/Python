import datetime
from contracheque import contracheque
from setor import setor
from fundionario import funcionario
class funcionario1:
    func= funcionario(nome="maria joaquin",setor=None,data_nacimento=datetime.date(1990,6,3),sexo="feminino",cargo="gerente")
# Agregacao do setor
    setor=setor(nome="setor da TI",gerente=func)
    contracheque_func=contracheque(funcionario=func,possui_vale_alimentacao=True)
    print(func.nome,func.data_nacimento,func.sexo,func.cargo)
    print(func.get_idade())
    print(contracheque_func.folha_pagemento())