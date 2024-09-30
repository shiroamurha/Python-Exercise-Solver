```
n = int(input("Número: "))
produto = 1
for i in range(1, n+1):
    print(i, end=' ')
    produto *= i
print("\nProduto:", produto)

