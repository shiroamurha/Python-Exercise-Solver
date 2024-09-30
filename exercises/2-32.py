valor = float(input("Digite o valor da prestação: "))
taxa = float(input("Digite a taxa: "))
tempo = float(input("Digite o tempo em meses: "))
prestacao = valor + (valor * (taxa * 0.01) * tempo)
print("O valor da prestação em atraso é: R$%.2f" % prestacao)

