class CarrinhoDeCompras:
  def __init__(self): 
    self.produtos = []
  
  def inserir_produtos(self, produto):
    self.produtos.append(produto)

  def listar_produtos(self):
    for produto in self.produtos:
      print(f'Produto: {produto.nome}. Valor: R${produto.valor}')
  def soma_total (self):
      soma = 0
      for produto in self.produtos:
        soma += produto.valor
      return soma