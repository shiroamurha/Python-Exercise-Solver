```
n = int(input("Insira um valor: "))
soma_pares = 0
produto_impares = 1

for i in range(1, n + 1):
    if i % 2 == 0:
        soma_pares += i
    else:
        produto_impares *= i

print("Soma dos pares:", soma_pares)
print("Produto dos impares:", produto_impares)

