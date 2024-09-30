```
n = int(input())
while n > 0:
    raiz = int(n**0.5)
    if raiz*raiz == n:
        print(n, "é um quadrado perfeito.")
    else:
        print(n, "não é um quadrado perfeito.")
    n = int(input())

