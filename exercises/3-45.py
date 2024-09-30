```
n = []
for i in range(10):
    while True:
        x = int(input(f"Digite o {i+1}º número: "))
        if x > 0:
            n.append(x)
            break
        else:
            print("Número inválido, tente novamente.")

print(f"O maior número é: {max(n)}")
print(f"O menor número é: {min(n)}")

n = int(input("Digite um valor positivo: "))
for i in range(1, n+1):
    print(i)
```

