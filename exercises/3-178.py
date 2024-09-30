```
n = int(input("Quantos valores você deseja inserir? "))
lista = []
for i in range(n):
    valor = int(input(f"Insira o {i+1}º valor: "))
    lista.append(valor)
for i in range(len(lista)):
    if lista[i] % (i+1) == 0:
        print(lista[i])
```

