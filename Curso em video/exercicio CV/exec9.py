num=int(input("digiti:"))
print('-' *12)
for i in range (11):
    if i!=0:
        print("{}*{:2}={}".format(num,i,(num*i)))
print("-"*12)    
