```
nome_produto = input("Nome do produto: ")
valor_compra = float(input("Valor da compra: "))

if valor_compra < 10:
    valor_venda = valor_compra * 1.7
elif 10 <= valor_compra < 30:
    valor_venda = valor_compra * 1.5
elif 30 <= valor_compra < 50:
    valor_venda = valor_compra * 1.4
else:
    valor_venda = valor_compra * 1.3

print(f"Nome do produto: {nome_produto}")
print(f"Valor da venda: R$ {valor_venda:.2f}")

