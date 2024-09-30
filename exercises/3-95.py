```
soma = 0
cont = 0
while True:
    num = int(input("Insira um número (-1 para parar): "))
    if num == -1:
        break
    soma += num
    cont += 1
if cont == 0:
    print("Nenhum número foi introduzido.")
else:
    media = soma / cont
    print("Média:", media)

