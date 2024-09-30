```
n = []
soma = 0
cont = 0
for i in range(8):
    num = float(input(f"Digite o {i+1}º valor: "))
    n.append(num)
    soma += num
    if num > 20:
        cont += 1
media = soma / 8
media_maior = sum([x for x in n if x > 20]) / cont
print(f"Soma dos valores: {soma}")
print(f"Média dos valores: {media}")
print(f"Média dos valores maiores que 20: {media_maior}")

