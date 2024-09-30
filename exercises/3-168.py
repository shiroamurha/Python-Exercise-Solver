```
produto = []
while True:
    nome = input("Nome do produto: ")
    qtd_produzida = int(input("Quantidade produzida: "))
    qtd_vendida = int(input("Quantidade vendida: "))
    estoque = qtd_produzida - qtd_vendida
    produto.append([nome, estoque])
    resposta = input("Deseja adicionar outro produto? (S/N): ")
    if resposta.upper() != "S":
        break

for p in produto:
    if p[1] < 50:
        print(f"Produto: {p[0]}, Estoque: {p[1]} - Estoque baixo!")
    else:
        print(f"Produto: {p[0]}, Estoque: {p[1]}")

maior_estoque = max(produto, key=lambda x: x[1])
print(f"Produto com maior estoque: {maior_estoque[0]}, Estoque: {maior_estoque[1]}")
```

