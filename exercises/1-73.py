```
diaria = float(input("Valor da diária por apartamento: "))
numero_apartamentos = int(input("Número de apartamentos do hotel: "))

diaria_promocional = diaria * 0.75
valor_total_100 = diaria * numero_apartamentos
valor_total_70 = diaria_promocional * numero_apartamentos
valor_perdido = valor_total_100 - valor_total_70

print("Valor promocional da diária: R$ {:.2f}".format(diaria_promocional))
print("Valor total a ser arrecadado caso a ocupação total seja atingida: R$ {:.2f}".format(valor_total_100))
print("Valor total a ser arrecadado caso a ocupação seja de 70%: R$ {:.2f}".format(valor_total_70))
print("Valor que o hotel deixará de arrecadar em virtude da promoção, caso a ocupação atinja 100%: R$ {:.2f}".format(valor_perdido))
```

