```
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())

soma1 = n1 + n2
soma2 = n3 + n4

if soma1 == soma2:
    print(n1, n2, n3, n4)
    print(soma1, soma2)
else:
    if soma1 % 2 == 0:
        print("Soma 1 é par")
    else:
        print("Soma 1 é ímpar")
    if soma2 % 2 == 0:
        print("Soma 2 é par")
    else:
        print("Soma 2 é ímpar")

