```
n = [int(input()) for _ in range(20)]
soma = 0
for num in n:
    if num ** 2 < 225:
        soma += num
print(soma)

