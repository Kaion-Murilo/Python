
from multiprocessing.connection import Client
from banco import Banco 
from cliente import Cliente
from conta import ContaCorrente, ContaPoupanca

banco = Banco()

cli1 = Cliente('Maria', 30)
cli2 = Cliente('José', 30)
cli3 = Cliente('Edjane', 32)

conta1 = ContaPoupanca(123, 123, 0)
conta2 = ContaPoupanca(231, 231, 0)
conta3 = ContaPoupanca(312, 312, 0)

cli1.inserir_conta(conta1)
cli2.inserir_conta(conta2)
cli3.inserir_conta(conta3)

banco.inserir_cliente(cli1)
banco.inserir_conta(conta1)

banco.inserir_cliente(cli2)
banco.inserir_conta(conta2)

banco.inserir_cliente(cli3)
banco.inserir_conta(conta3)

if banco.autenticar(cli1):
  cli1.Conta.Depositar(0)
  cli1.conta.sacar(500)

else: 
  print('Cliente não autorizado.')