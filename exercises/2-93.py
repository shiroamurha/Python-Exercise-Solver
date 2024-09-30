```
litros = float(input())
combustivel = int(input())
preco = float(input())

if combustivel == 1:
    if litros <= 20:
        valor = litros * preco
    else:
        valor = (20 * preco) + ((litros - 20) * preco * (1 - 0.03))
elif combustivel == 2:
    if litros <= 15:
        valor = litros * preco
    else:
        valor = (15 * preco) + ((litros - 15) * preco * (1 - 0.035))

print(f'Litros: {litros:.2f}')
print(f'Preço: {preco:.2f}')
print(f'Valor a ser pago: {valor:.2f}')
```

