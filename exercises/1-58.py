```
km_inicio = float(input())
km_fim = float(input())
litros = float(input())
receita = float(input())

km_total = km_fim - km_inicio
consumo = km_total / litros
lucro = receita - (litros * 2.5)

print(f"{consumo:.0f}")
print(f"{lucro:.0f}")
```

