```
def digito_verificador(numero):
    numero_inverso = int(str(numero)[::-1])
    soma = 0
    for i, digito in enumerate(str(numero)):
        soma += int(digito) * (i + 1)
    return str(soma)[-1]

