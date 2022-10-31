nome = str(input("Qual é seu nome?"))
if nome=='gustavo':
    print("noe bonito")
elif nome == "pedro" or nome == "Maria" or nome == 'pedro':
    print("Seu nome e muito plpupar no Brasil")
elif nome in 'Ana Claudia Jessica julia':
    print("bom nome feminino")
# else :
#     print("seu nome e bem normal")
print("tenha um bom dia ,{}".format(nome))
