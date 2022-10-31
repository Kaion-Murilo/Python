f=str(input("digiti:")).strip()
v=f.find("Santo")
if v==0:
    print('A frase comeca  com Santos ')
else:
    print('A frase nao comeca com santos')
    
print(f[:5].upper() == "SANTO")