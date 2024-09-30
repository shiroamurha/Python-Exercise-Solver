```
valor_investido = 0
juros_pagos = 0

while True:
    codigo_cliente = int(input("Código do cliente: "))
    tipo_conta = int(input("Tipo da conta (1, 2, 3 ou 4): "))
    valor_investido_atual = float(input("Valor investido: "))

    if tipo_conta == 1:
        juros = valor_investido_atual * 0.015
    elif tipo_conta == 2:
        juros = valor_investido_atual * 0.02
    elif tipo_conta == 3:
        juros = valor_investido_atual * 0.04
    elif tipo_conta == 4:
        juros = valor_investido_atual * 0.05
    else:
        print("Tipo de conta inválido")
        continue

    valor_investido += valor_investido_atual
    juros_pagos += juros

    print(f"Rendimento mensal: {juros:.2f}")
    print(f"Valor investido: {valor_investido:.2f}")
    print(f"Total de juros pagos: {juros_pagos:.2f}\n")

    resposta = input("Deseja continuar? (S/N): ")
    if resposta.upper() != "S":
        break

print(f"Total investido: {valor_investido:.2f}")
print(f"Total de juros pagos: {juros_pagos:.2f}")

