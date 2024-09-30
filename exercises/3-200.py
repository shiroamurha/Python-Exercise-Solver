```
nome = input("Nome da família: ")
n_filhos = int(input("Número de filhos: "))
total = 0
while n_filhos > 0:
    escolaridade = input("Escolaridade (pré-escola, 1o ciclo do ensino fundamental, 2o ciclo do ensino fundamental, Ensino Médio): ")
    valor = 0
    if escolaridade == "pré-escola":
        valor = 300
    elif escolaridade == "1o ciclo do ensino fundamental":
        valor = 400
    elif escolaridade == "2o ciclo do ensino fundamental":
        valor = 500
    elif escolaridade == "Ensino Médio":
        valor = 600
    desconto = 0
    if n_filhos > 1:
        desconto = valor * 0.1
    elif n_filhos > 2:
        desconto = valor * 0.2
    elif n_filhos > 3:
        desconto = valor * 0.3
    elif n_filhos > 4:
        desconto = valor * 0.4
    valor_desconto = valor - desconto
    total += valor_desconto
    n_filhos -= 1
print("O valor total a ser pago pela família é: R$%.2f" % total)

