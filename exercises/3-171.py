```
nome = ''
total = 0
while True:
    dias = int(input('Número de dias: '))
    preco_diaria = 30
    taxa_servicos = 0
    if dias < 10:
        taxa_servicos = 15
    else:
        taxa_servicos = 8
    total_gasto = preco_diaria * dias + taxa_servicos
    print(f'Nome: {nome}\nTotal gasto: R${total_gasto:.2f}')
    total += total_gasto
    resposta = input('Deseja inserir um novo cadastro? (S/N): ')
    if resposta.upper() != 'S':
        break
print(f'Total ganho pela pousada: R${total:.2f}')

