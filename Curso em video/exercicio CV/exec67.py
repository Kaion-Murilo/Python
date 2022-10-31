num=10
while True:
    print("====="*20)
    num = int(input("DIGITI VALOR : "))
    print("-=-"*20)
    if num >0:
        for i in range(1,11):
            print(f"{num} * {i} = {num * i}" )
    else:
        break
print("FIM")