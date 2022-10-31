from time import sleep
print("-"*20)
print("SEQUENCIA DE FIBINATE")
print("-"*20)
n = int(input("digiti:"))
t1 = 0 
t2 = 1
print("{} => {} ".format(t1,t2),end="")
cont=3
print("-"*20)
while 0 <=n:
     t3=t1+t2
     print("{}".format(t3),end="->")
     t1=t2
     t2=t3
     cont +=1
print("-"*20)
print("FIM")
print("-"*20)
