```
nome_cliente = ''
total_clientes = 0
combustivel_alcool = 0
combustivel_gasolina = 0
combustivel_diesel = 0

while True:
    cliente = input('Nome do cliente: ')
    while True:
        combustivel = int(input('Tipo de combustível (1. álcool, 2. gasolina, 3. diesel, 4. finalizar): '))
        if combustivel == 1:
            print('Álcool')
            combustivel_alcool += 1
            break
        elif combustivel == 2:
            print('Gasolina')
            combustivel_gasolina += 1
            break
        elif combustivel == 3:
            print('Diesel')
            combustivel_diesel += 1
            break
        elif combustivel == 4:
            print('MUITO OBRIGADO por participar da pesquisa de opinião')
            print(f'Total de clientes: {total_clientes + 1}')
            print(f'Quantidade de clientes que abasteceram álcool: {combustivel_alcool}')
            print(f'Quantidade de clientes que abasteceram gasolina: {combustivel_gasolina}')
            print(f'Quantidade de clientes que abasteceram diesel: {combustivel_diesel}')
            break
        else:
            print('Código inválido. Por favor, tente novamente.')

    total_clientes += 1

print('Fim do programa')
```

