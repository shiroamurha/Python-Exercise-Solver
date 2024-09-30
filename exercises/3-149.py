soma = 0
contador = 0

while True:
    num = float(input("Digite um número positivo (ou 0 para parar): "))
    if num > 0:
        soma += num
        contador += 1
    elif num == 0:
        break

if contador > 0:
    media = soma / contador
    print(f"A média dos números digitados é {media:.2f}")
else:
    print("Nenhum número foi digitado.")

