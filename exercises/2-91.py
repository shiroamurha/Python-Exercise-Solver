nome = input("Digite o primeiro nome do cliente: ")
valor = float(input("Digite o valor da conta: "))

if nome[0].upper() in ['A', 'D', 'M', 'S']:
    valor *= 0.7
    print(f"O valor da conta é {valor:.2f} com desconto.")
else:
    print("Que pena. Nesta semana o desconto não é para seu nome. Mas continue nos prestigiando, que sua vez chegará.")

