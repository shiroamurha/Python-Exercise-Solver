```
def moedas(valor):
    notas = [100, 50, 20, 10, 5, 2, 1]
    moedas = [0.50, 0.25, 0.10, 0.05, 0.01]
    resultado = []
    for nota in notas:
        quantidade = int(valor / nota)
        resultado.append(quantidade)
        valor -= quantidade * nota
    for moeda in moedas:
        quantidade = int(valor / moeda)
        resultado.append(quantidade)
        valor -= quantidade * moeda
    return resultado

valor = float(input("Digite o valor: "))
print(moedas(valor))
```

