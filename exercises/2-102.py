```
n = int(input("Digite um número: "))
if n <= 1:
    print("Não é primo")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Não é primo")
            break
    else:
        print("É primo")

