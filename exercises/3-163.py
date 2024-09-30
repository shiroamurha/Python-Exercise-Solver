n = int(input("Digite o primeiro número: "))
m = int(input("Digite o segundo número: "))
while m != 0:
    n, m = m, n % m
print("O M.D.C. é:", n)

