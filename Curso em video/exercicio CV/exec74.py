from random import randint
from smtpd import MailmanProxy
a=(randint(1,1000))
b=(randint(1,1000))
c=(randint(1,1000))
d=(randint(1,1000))
e=(randint(1,1000))
num=(a,b,c,d,e)
print(num)
for c in range (len(num)):
    print(num[c])
    if c==0:
        Maior=num[c]
        Menor=num[c]
    if num[c]> Maior:
        Maior=num[c]
    if num[c]< Menor:
        Menor=num[c]
print(Maior)
print(Menor)