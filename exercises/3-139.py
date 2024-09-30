```
n = int(input())
if n < 2:
    print("Não é primo")
elif n == 2:
    print("É primo")
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Não é primo")
            break
    else:
        print("É primo")

