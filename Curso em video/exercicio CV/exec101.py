def voto (ano):
    from datetime import date 
    atual=date.today().year
    idade=atual-ano
    if idade<16:
        return f"com {idade} anos nao vota"
    if 16<=idade<18 or idade>65:
        return f"com {idade} anos voto opivional"
    else:
        return f"com {idade} anos voto  obrigatorio"
nasc=int(input("em que ano voce naceu?"))
print(voto(nasc))