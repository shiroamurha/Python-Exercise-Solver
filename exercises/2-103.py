```
preco = {
    101: 3.0,
    201: 5.0,
    202: 6.0,
    301: 4.0,
    302: 5.0,
    500: 2.0
}

pedido = {}
total = 0.0

while True:
    codigo = int(input("Código do item (ou 0 para sair): "))
    if codigo == 0:
        break
    quantidade = int(input("Quantidade: "))
    if codigo in preco:
        total += preco[codigo] * quantidade
        if codigo in pedido:
            pedido[codigo] += quantidade
        else:
            pedido[codigo] = quantidade
    else:
        print("Código não encontrado!")

print("Pedido:")
for codigo, quantidade in pedido.items():
    print(f"{preco[codigo]} x {quantidade} = {preco[codigo] * quantidade:.2f}")
print(f"Total: {total:.2f}")

