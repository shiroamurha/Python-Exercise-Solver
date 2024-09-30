```
n = int(input("Digite um número: "))
while True:
    if n % 6 == 0:
        print(n**2)
        break
    print(n**2)
    n = int(input("Digite um número: "))

