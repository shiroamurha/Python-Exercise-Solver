```
n = 1
cont = 0
while n != 0:
    n = int(input("Digite um número (0 para sair): "))
    if 100 <= n <= 200:
        cont += 1
print(f"Foram digitados {cont} números entre 100 e 200.")

