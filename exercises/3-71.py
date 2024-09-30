numeros = []

for i in range(20):
    numeros.append(int(input("Digite um número: ")))

soma_positivos = sum([x for x in numeros if x > 0])
quantidade_negativos = sum([1 for x in numeros if x < 0])

print("Soma dos positivos:", soma_positivos)
print("Quantidade de números negativos:", quantidade_negativos)

