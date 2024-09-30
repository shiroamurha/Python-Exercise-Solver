numeros = []
soma = 0

while True:
    n = int(input("Insira um número inteiro e positivo (ou 0 para parar): "))
    if n == 0:
        break
    if n > 0:
        if n % 3 == 0:
            numeros.append(n)
            soma += n
    else:
        print("Número inválido. Por favor, insira um número inteiro e positivo.")

if len(numeros) > 0:
    media = soma / len(numeros)
    print("A média dos números múltiplos de 3 é: ", media)
else:
    print("Nenhum número múltiplo de 3 foi encontrado.")

