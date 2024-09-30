n = 0
while True:
    x = int(input("Digite um número (ou 0 para parar): "))
    if x > 0:
        n += 1
    else:
        break
print(f"Você digitou {n} números.")

