```
n = int(input())
triplos = []
for _ in range(n):
    num = int(input())
    triplo = num * 3
    triplos.append(triplo)
maior = max(triplos)
print(triplos)
print(f"Maior: {max([i for i in zip(triplos, [f"{i} - {i * 3}" for i in triplos]) if i[0] == maior][0][1])}")

