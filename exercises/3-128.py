pares = 0
impares = 0

for i in range(15):
    num = int(input("Digite o número {}: ".format(i+1)))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Pares: {} | Ímpares: {}".format(pares, impares))

