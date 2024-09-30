```
ano = int(input("Ano do modelo: "))
peso = float(input("Peso do modelo: "))

if ano <= 1970:
    if peso < 1200:
        classe = 1
        taxa_registro = 16.50
    elif 1200 <= peso <= 1700:
        classe = 2
        taxa_registro = 25.50
    else:
        classe = 3
        taxa_registro = 46.50
elif 1971 <= ano <= 1979:
    if peso < 1200:
        classe = 4
        taxa_registro = 27.00
    elif 1200 <= peso <= 1700:
        classe = 5
        taxa_registro = 30.50
    else:
        classe = 6
        taxa_registro = 52.50
else:
    if peso < 3600:
        classe = 7
        taxa_registro = 19.50
    else:
        classe = 8
        taxa_registro = 52.50

print(f"Classe: {classe}")
print(f"Taxa de registro: R$ {taxa_registro:.2f}")
```

