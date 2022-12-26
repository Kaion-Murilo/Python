from random import randint

num=(randint(1,1000),randint(1,1000),randint(1,1000),randint(1,1000),randint(1,1000))
print("Os valores sorteados foram: ",num)

# for c in range (len(num)):
#     print(num[c])
#     if c==0:
#         Maior=num[c]
#         Menor=num[c]
#     if num[c]> Maior:
#         Maior=num[c]
#     if num[c]< Menor:
#         Menor=num[c]
# print(Maior)
# print(Menor)
print(f"\nO maior valor e :{max(num)}")
print(f"O menor valor e :{min(num)}")