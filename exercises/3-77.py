```
n = 0
soma = 0
cont = 0
for i in range(10):
    x = float(input())
    if 20 <= x <= 50 and x % 2 == 0:
        soma += x
        cont += 1
    elif 20 <= x <= 50:
        n += 1
media = soma / cont if cont > 0 else 0
print(f"Média dos valores pares entre 20 e 50: {media:.2f}")
print(f"Quantidade de valores entre 20 e 50: {cont}")
print(f"Quantidade de valores fora do intervalo: {n}")
```

