# Se o ano for uniformemente divisível por 4, vá para a etapa 2. Caso contrário, vá para a etapa 5.
# Se o ano for uniformemente divisível por 100, vá para a etapa 3. Caso contrário, vá para a etapa 4.
# Se o ano for uniformemente divisível por 400, vá para a etapa 4. Caso contrário, vá para a etapa 5.
# O ano é bissexto (tem 366 dias).
# O ano não é um ano bissexto (tem 365 dias).
from datetime import date
ano=int(input("Digiti um ano digiti zero se queiser o ano atual : "))
if ano == 0:
    ano= date.today().year 
if ano%4==0 and ano % 100 !=0 or ano % 400 ==0:
    print("O ano {} é bisexto".format(ano))
else:
    print("O ano de {} nao e um ano bisexto".format(ano))