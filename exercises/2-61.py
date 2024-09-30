```
cores = {
    'azul': 10.00,
    'rosa': 25.00,
    'verde': 35.00,
    'vermelho': 50.00
}

cor = input("Insira a cor do DVD: ")
quantidade = int(input("Insira a quantidade de DVDs que deseja levar: "))

preco = cores.get(cor.lower(), "Cor não encontrada")
valor_total = preco * quantidade

print(f"Você irá levar {quantidade} DVDs de cor {cor}.")
print(f"O valor do DVD é R$ {preco:.2f}.")
print(f"O valor total que você irá pagar é R$ {valor_total:.2f}.")

