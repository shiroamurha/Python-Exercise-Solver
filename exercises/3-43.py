```
n = int(input())
contador_intervalo = 0
contador_fora_intervalo = 0
for i in range(n):
    valor = int(input())
    if 10 <= valor <= 30:
        contador_intervalo += 1
    else:
        contador_fora_intervalo += 1
print(f"{contador_intervalo} estão no intervalo")
print(f"{contador_fora_intervalo} estão fora do intervalo")
```

