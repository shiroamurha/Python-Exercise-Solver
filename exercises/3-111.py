```
salarios = []
filhos = []
while True:
    salario = float(input('Salário: '))
    filho = int(input('Número de filhos: '))
    salarios.append(salario)
    filhos.append(filho)
    continua = int(input('Deseja continuar o cadastro? 1. Sim 2. Não '))
    if continua == 2:
        break

media_salario = sum(salarios) / len(salarios)
media_filhos = sum(filhos) / len(filhos)
maior_salario = max(salarios)
porcentagem = (salarios.count(200) / len(salarios)) * 100

print(f'Média do salário: {media_salario:.2f}')
print(f'Média do número de filhos: {media_filhos:.2f}')
print(f'Maior salário: {maior_salario:.2f}')
print(f'Percentual de pessoas com salário de até R$200,00: {porcentagem:.2f}%')

