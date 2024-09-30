```
n = int(input())
while n != -999:
    print("Divisores de", n, ":", end=" ")
    for i in range(1, n+1):
        if n % i == 0:
            print(i, end=" ")
    print()
    n = int(input())

