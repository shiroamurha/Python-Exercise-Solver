```
n = int(input("Insira um valor: "))
soma_pares = 0
produto_impares = 1
for i in range(100, n+1):
    if i % 2 == 0:
        soma_pares += i
    else:
        produto_impares *= i
print("A soma dos valores pares é: ", soma_pares)
print("O produto dos valores ímpares é: ", produto_impares)
```

