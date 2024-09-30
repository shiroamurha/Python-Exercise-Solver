```
codigo = {
    101: 3.0,
    201: 5.0,
    202: 6.0,
    301: 4.0,
    302: 5.0,
    500: 2.0
}

pessoas = int(input())
total = 0

for _ in range(pessoas):
    pessoa = {}
    quantidade = {}

    pessoa['nome'] = input()
    quantidade['cachorrouente'] = int(input())
    quantidade['bauru_simple'] = int(input())
    quantidade['bauru_ovo'] = int(input())
    quantidade['hamburguer'] = int(input())
    quantidade['cheeseburguer'] = int(input())
    quantidade['refrigerante'] = int(input())

    total_pedido = 0
    for item, quant in quantidade.items():
        if item == 'cachorrouente':
            total_pedido += quant * 3.0
        elif item == 'bauru_simple':
            total_pedido += quant * 5.0
        elif item == 'bauru_ovo':
            total_pedido += quant * 6.0
        elif item == 'hamburguer':
            total_pedido += quant * 4.0
        elif item == 'cheeseburguer':
            total_pedido += quant * 5.0
        elif item == 'refrigerante':
            total_pedido += quant * 2.0

    total += total_pedido

print(f'O valor total a ser pago é R${total:.2f}')

