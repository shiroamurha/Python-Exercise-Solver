```
tamanho = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
litros_necessarios = tamanho / 3
latas_necessarias = -(-litros_necessarios // 18)  # divisão inteira
preco_total = latas_necessarias * 80
print(f"Você precisará de {latas_necessarias} latas de tinta e o preço total será de R${preco_total:.2f}.")

