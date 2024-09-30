n = int(input())
i = 1
while True:
    j = i
    k = i + 1
    while k <= n:
        if i * j * k == n:
            print("Sim")
            break
        k += 1
    else:
        print("Não")
    i += 1

