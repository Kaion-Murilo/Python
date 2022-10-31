import os 
os.system('cls')
print("oi")

arquivo=open('dec.txt','w')
x=0

for i in range (1,101):
    x=101-i
    arquivo.write(str(x) +'; ')
print(type(arquivo))
arquivo.close
