```
def questao171():
    produto_impares = 1
    soma_pares = 0
    while True:
        num = int(input("Insira um número inteiro e positivo (ou 0 para parar): "))
        if num == 0:
            break
        if num % 2 == 0:
            soma_pares += num
        else:
            produto_impares *= num
    print(f"Produto dos números ímpares: {produto_impares}")
    print(f"Soma dos números pares: {soma_pares}")

def questao172():
    total = 0
    while True:
        pedido = input("Insira o número do pedido (ou 0 para parar): ")
        if pedido == '0':
            break
        data = input("Insira a data do pedido (dia, mes, ano): ")
        preco = float(input("Insira o preço unitário: "))
        quantidade = int(input("Insira a quantidade: "))
        total += preco * quantidade
    print(f"Valor total da compra: {total}")

questao171()
questao172()

