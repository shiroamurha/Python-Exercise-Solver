```
idades = []
pesos = []
alturas = []
sexos = []
olhos = []
cabelos = []

while True:
    sexo = input("Insira o sexo (M/F): ")
    olho = input("Insira a cor dos olhos (A/V/C): ")
    cabelo = input("Insira a cor dos cabelos (L/C/P): ")
    idade = float(input("Insira a idade: "))
    altura = float(input("Insira a altura: "))
    peso = float(input("Insira o peso: "))

    idades.append(idade)
    pesos.append(peso)
    alturas.append(altura)
    sexos.append(sexo)
    olhos.append(olho)
    cabelos.append(cabelo)

    continuar = input("Deseja continuar? (S/N): ")
    if continuar.upper() != "S":
        break

media_idade = sum(idades) / len(idades)
media_peso = sum(pesos) / len(pesos)
media_altura = sum(alturas) / len(alturas)

feminino = sexos.count("F")
masculino = sexos.count("M")
total = len(sexos)

porcentagem_feminino = (feminino / total) * 100
porcentagem_masculino = (masculino / total) * 100

verdes_cabelos_louros = [i for i, (olho, cabelo) in enumerate(zip(olhos, cabelos)) if olho == "V" and cabelo == "L"]
quantidade = len(verdes_cabelos_louros)

print(f"Média da idade: {media_idade}")
print(f"Média do peso: {media_peso}")
print(f"Média da altura: {media_altura}")
print(f"Porcentagem de pessoas do sexo feminino: {porcentagem_feminino}%")
print(f"Porcentagem de pessoas do sexo masculino: {porcentagem_masculino}%")
print(f"Pessoas com olhos verdes e cabelos louros: {quantidade}")
```

