```
h = float(input("Altura: "))
if input("Sexo (M/F): ") == "M":
    peso_ideal = (72.7*h) - 58
else:
    peso_ideal = (62.1*h) - 44.7

peso = float(input("Peso: "))
if peso > peso_ideal:
    print("Peso acima do ideal")
elif peso < peso_ideal:
    print("Peso abaixo do ideal")
else:
    print("Peso dentro do ideal")
```

