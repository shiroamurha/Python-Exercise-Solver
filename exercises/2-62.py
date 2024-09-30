```
morangos = float(input())
maças = float(input())
morango_preco = 0
maça_preco = 0
total_preco = 0

if morangos <= 5:
    morango_preco = morangos * 5
else:
    morango_preco = 5 * 5 + (morangos - 5) * 4

if maças <= 5:
    maça_preco = maças * 3
else:
    maça_preco = 5 * 3 + (maças - 5) * 2

total_preco = morango_preco + maça_preco

if total_preco > 35 or morangos + maças > 8:
    total_preco *= 0.8

print(f'Morango: R${morango_preco:.2f}')
print(f'Maça: R${maça_preco:.2f}')
print(f'Total: R${total_preco:.2f}')
```

