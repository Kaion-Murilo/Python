import urllib.request
try:
    site = urllib.request.urlopen('http://pudin.com.br')
except urllib.error.URLError:
    print("o site nao esta disponivel")
else:
    print("consegui acesso ao site")