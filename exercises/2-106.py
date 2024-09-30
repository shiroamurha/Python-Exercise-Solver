```
salario = float(input("Salário: "))
gasto = float(input("Valor gasto com cesta básica: "))

percentual = (gasto / salario) * 100

if percentual <= 25:
    print("Esbanjador")
elif 26 <= percentual <= 53:
    print("Gastador")
elif 54 <= percentual <= 75:
    print("Comedido")
elif 76 <= percentual <= 95:
    print("Essencial")
else:
    print("Essencial")

