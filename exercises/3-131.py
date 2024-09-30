```
idades = []
pesos = []
for i in range(20):
    idade = int(input("Idade: "))
    idades.append(idade)
    peso = float(input("Peso: "))
    pesos.append(peso)

idades.sort()
pesos.sort()

for i in range(1, 31):
    media = sum(peso for peso in pesos if idades[pesos.index(peso)] >= i and idades[pesos.index(peso)] < i+10) / len([peso for peso in pesos if idades[pesos.index(peso)] >= i and idades[pesos.index(peso)] < i+10])
    print(f"Faixa etária {i}-{i+9}: {media:.2f}")
    
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
```

