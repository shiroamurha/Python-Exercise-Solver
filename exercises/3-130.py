134:
```
n = 0
maiores_30 = 0
while n < 15:
    x = float(input("Digite um número: "))
    n += 1
    if x > 30:
        maiores_30 += 1
print(f"Quantidade de números maiores que 30: {maiores_30}")
```

135:
```
soma_positivos = 0
cont_negativos = 0
for i in range(20):
    x = float(input("Digite um número: "))
    if x > 0:
        soma_positivos += x
    elif x < 0:
        cont_negativos += 1
print(f"Soma dos positivos: {soma_positivos}")
print(f"Total de números negativos: {cont_negativos}")
```

