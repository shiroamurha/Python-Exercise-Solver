```
produto = float(input("Valor do produto: "))
desconto = produto * 0.09
novo_valor = produto - desconto

print(f"Valor do produto: R$ {produto:.2f}")
print(f"Novo valor do produto: R$ {novo_valor:.2f}")
print(f"Desconto: R$ {desconto:.2f}")

