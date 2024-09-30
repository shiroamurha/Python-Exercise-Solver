```
n = 1
primos = 0
while n > 0:
    n = int(input())
    if n <= 0:
        break
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        primos += 1
print(primos)

