frasett='curso em video'
# len(frase)
# frase.count("o")#contar quabtas  letras o tem
frasett.find("deo")#onde ccomesa a str
# curso in frase
# farse,repalce('python','android')
# frase.upper()#tudo em maiusculo
# frase.lower()#tudo em minusculor
# farse.capitalize()#so a primeira letra em maiuscula
# frase.title() #palavras comecao com maisculas
#   Espacos
# #frase.strip()#remover os espaso desne
# frase.rstrip()#remover espacos da ddireita
# frase.lstrip()#remover espacos da esquerda
#separar frases
#frase.split()#vai dividir por espasos
#Juncao
#''.join(frase)

frase = "  curso em Video Python  "
print(frase[3])
print(frase[3:13])
print(frase[13:])
print(frase[1:15:2])
print(frase[::2])
print(frase.count('o'))
print(frase.count('O'))
print(len(frase))
print(len(frase.strip()))
print(frase.replace('Python','Android'))
print("Curso" in frase)
print(frase.find("Curso"))
print(frase.find("video"))
print(frase.lower().find("video"))
print(frase.split())
div=frase.split()
print(div[2][3])
