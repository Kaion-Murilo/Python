from datetime import datetime
import os
os.system("cls")
"""
class pokemon:
    def __init__(self,nome:str,idade:int,poder:str):
        self.nome=nome 
        self.idade=idade
        self.poder=poder
    def falar(self):
        print(f"olar o meu nome e {self.nome}.tenho{self.idade}")
    def andar(self, distancia:float):
        print(f"sai com a equipe reoquete e percorrremos {distancia}KM,para livrar mundo da escuridao e pegar o pikachu")
    def comer(self, macarroo:str):
        print(f"estou comendo seu{macarroo}")
#estanciar um obijeto da classe pokemon
pokemon=pokemon(nome='Meow',idade=2,poder='aranhar')
pokemon.falar()
pokemon.andar(10)
pokemon.comer("macarroo")        

class Pokemon:
  def __init__(self, nome: str, idade: str, poder:str):
    self.nome = nome
    self.idade = idade
    self.poder = poder 

  def falar(self):
    print(f'Olá, meu nome é {self.nome}. Tenho {self.idade}')
  def andar(self, distancia:float):
    print(f'Saí com a equipe Rocket, e percorremos {distancia} KM, para livrar o mundo da escuridão e pegar o Pikachu')
  def comer(self, macarrao: str):
    print(f'Estou comendo meu {macarrao}')
#Instanciar um objeto da classe Pokemon
pokemon = Pokemon(nome='Meow', idade='2 anos',poder='Arranhar')
pokemon.falar()
pokemon.andar(5000)
pokemon.comer('Macarrão')
"""
# prjeto semplespessoa
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
class funcionario:
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

class funcionario1 :
    func= funcionario(nome="maria joaquin",setor=None,data_nacimento=datetime.date(1990,6,3),sexo="feminino",cargo="gerente")
# Agregacao do setor
    setor=setor(nome="setor da TI",gerente=func)
    contracheque_func=contracheque(funcionario=func,possui_vale_alimentacao=True)
    print(func.nome,func.data_nacimento,func.sexo,func.cargo)
    print(func.get_idade())
    print(contracheque_func.imprir_contracheque())