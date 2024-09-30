valor = float(input("Insira o valor da prestação: "))
taxa = float(input("Insira a taxa de juros: "))
tempo = float(input("Insira o tempo em meses: "))

prestacao = valor + (valor * (taxa/100)*tempo)

print("O valor da prestação em atraso é: ", prestacao)

