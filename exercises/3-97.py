```
n = 0
soma = 0
minimo = None
maximo = None

while True:
    x = input("Insira um valor (ou 'fim' para parar): ")
    if x == 'fim':
        break
    x = float(x)
    n += 1
    soma += x
    if minimo is None or x < minimo:
        minimo = x
    if maximo is None or x > maximo:
        maximo = x

if n > 0:
    media = soma / n
    print(f"Mínimo: {minimo}")
    print(f"Máximo: {maximo}")
    print(f"Média: {media}")
else:
    print("Nenhum valor foi digitado.")

