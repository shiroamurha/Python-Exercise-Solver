produto_pares = 1
for i in range(10):
    num = int(input("Insira um número inteiro e positivo: "))
    if num % 2 == 0:
        print(f"O número {num} é par.")
        produto_pares *= num
print(f"O produto dos números pares é {produto_pares}.")

