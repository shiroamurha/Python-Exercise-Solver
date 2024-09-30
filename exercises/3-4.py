soma = 0
cont = 0

for i in range(1, 51):
    if i % 2 == 0:
        soma += i
        cont += 1

print("A soma dos números pares é:", soma)
print("Foram utilizados", cont, "números para calcular a soma.")

