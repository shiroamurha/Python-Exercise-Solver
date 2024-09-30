Questão 208:
```
salario = float(input("Salário: "))
classe = int(input("Classe (1-7): "))

while classe >= 1 and classe <= 7:
    if classe == 1:
        bicho = salario * 2
    elif classe == 2:
        bicho = salario * 1.8
    elif classe == 3:
        bicho = salario * 1.5
    elif classe == 4:
        bicho = salario * 1.3
    elif classe == 5:
        bicho = salario * 1.1
    elif classe == 6:
        bicho = salario * 1.05
    elif classe == 7:
        bicho = 0

    salario_final = salario + bicho
    print(f"Salário final: {salario_final:.2f}")
    print(f"Classe: {classe} (Nível)")

    salario = float(input("Salário: "))
    classe = int(input("Classe (1-7): "))

print("Fim do programa.")
```

