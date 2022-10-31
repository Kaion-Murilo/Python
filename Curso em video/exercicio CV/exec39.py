from datetime import date
atual=date.today().year
nac=int(input("ano de nacimento: "))
idade=atual - nac
print("Quem naceu em {} tem {} anos em {}".format(nac,idade,atual))
if idade>18:
    d=idade-18
    ano=atual-d
    print("ja  pasoou {} anos da hora de se alistar ".format(d))
    print("seu alistamento foi em {}".format(ano))
if idade<18:
    d=18-idade
    
    print("Ainda falta {} anos para  voce se alistara".format(d))
if idade==18:
    print("ja e hora de se alistar ")
    