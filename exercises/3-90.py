```
nota1 = float(input("Insira a nota da 1ª avaliação: "))
while nota1 < 0 or nota1 > 10:
    print("Nota inválida")
    nota1 = float(input("Insira a nota da 1ª avaliação: "))

nota2 = float(input("Insira a nota da 2ª avaliação: "))
while nota2 < 0 or nota2 > 10:
    print("Nota inválida")
    nota2 = float(input("Insira a nota da 2ª avaliação: "))

media = (nota1 + nota2) / 2
print(f"A média é {media:.1f}")
```

