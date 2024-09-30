```
negativos = 0
intervalo = 0
maiores = 0
for i in range(15):
    num = float(input("Insira o número {}: ".format(i+1)))
    if num < 0:
        negativos += 1
    elif 15 <= num <= 45:
        intervalo += 1
    elif num > 100:
        maiores += 1
print("Quantidade de números negativos: ", negativos)
print("Quantidade de números entre 15 e 45: ", intervalo)
print("Quantidade de números maiores que 100: ", maiores)

