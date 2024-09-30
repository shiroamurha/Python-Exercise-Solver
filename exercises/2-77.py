months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

mes = int(input('Informe o mês (1-12): '))

if 1 <= mes <= 12:
    print(months[mes - 1])
else:
    print('Mês inválido')

