```
n = int(input())
if n < 2:
    print("Não primo")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Não primo")
            break
    else:
        print("Primo")

