palavras= ("aprendiz","programacao","linguagen",'python','curso',"futuro","mercado")
for p in palavras:
    print(f"\nna palavra {p.upper()} temos :> ",end="")
    for letras in p:
        if letras.lower() in "aeiou":
            print(letras,end=" ")