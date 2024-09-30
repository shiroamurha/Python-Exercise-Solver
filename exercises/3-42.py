x = 1
soma = 0
cont = 0
while True:
    valor = int(input("Insira um valor (ou 0 para parar): "))
    if valor == 0:
        break
    soma += valor
    cont += 1
    x += 1
if cont > 0:
    media = soma / cont
    print("A média dos valores entre 1 e", x, "é", media)
else:
    print("Nenhum valor foi informado.")

