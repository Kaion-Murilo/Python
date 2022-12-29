def aumento (preco,taxa,formato=False):
    res= preco+(preco*taxa/100)
    return res if formato is False else moeda(res)
def diminuir (preco,taxa,formato=False):
    res= preco - (preco*taxa/100)
    return res if formato is False else moeda(res)
def dobro (preco,formato=False):
    res= preco*2
    return res if formato is False else moeda(res)
def metade(preco,formato=False):
    res= preco/2
    return res if formato is False else moeda(res)
def moeda(preco=0,moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.',',')
def resumo (preco=0,taxa=10,taxar=5):
    print("-"*30)
    print("RESUMO DO VALOR".center(30))
    print("-"*30)
    print(f"preco analizado : \t{moeda(preco)}")
    print(f"dobro do preco: \t{dobro(preco,True)}")
    print(f"metade do preco: \t{metade(preco,True)}")
    print(f"com a {taxa}% de aumento : \t{aumento(preco,taxa,True)}")
    print(f"com a {taxar}% de diminuicao : \t{diminuir(preco,taxar,True)}")
    print("-"*30)