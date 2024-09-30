km = float(input("Insira o percurso em quilômetros: "))
tipo_carro = input("Insira o tipo do carro (A, B ou C): ")

if tipo_carro == "A":
    consumo = km / 12
    print(f"O consumo estimado do combustível é {consumo:.2f} litros.")
elif tipo_carro == "B":
    consumo = km / 9
    print(f"O consumo estimado do combustível é {consumo:.2f} litros.")
elif tipo_carro == "C":
    consumo = km / 8
    print(f"O consumo estimado do combustível é {consumo:.2f} litros.")
else:
    print("Tipo de carro inválido.")

