```
destino = input("Digite o destino: ")
if destino == "Região Norte":
    valor_ida = 500.00
    valor_volta = 900.00
elif destino == "Região Nordeste":
    valor_ida = 350.00
    valor_volta = 650.00
elif destino == "Região Centro-Oeste":
    valor_ida = 350.00
    valor_volta = 600.00
elif destino == "Região Sudeste":
    valor_ida = 300.00
    valor_volta = 500.00
elif destino == "Região Sul":
    valor_ida = 300.00
    valor_volta = 550.00
else:
    print("Destino não encontrado")
    valor_ida = 0.00
    valor_volta = 0.00
print("Valor da passagem ida: R$ {:.2f}".format(valor_ida))
print("Valor da passagem volta: R$ {:.2f}".format(valor_volta))
```

