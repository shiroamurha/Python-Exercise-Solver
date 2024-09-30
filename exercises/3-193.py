```
nome = ''
sexo = ''
idade = 0
peso = 0
altura = 0
atleta_mais_alto_masculino = ''
atleta_mais_pesada_feminino = ''
soma_idade = 0
qtd_atletas = 0
atleta_mais_jovem = ''

while True:
    nome = input('Nome: ')
    if nome == '@':
        break
    sexo = input('Sexo (M/F): ')
    idade = int(input('Idade: '))
    peso = float(input('Peso: '))
    altura = float(input('Altura: '))
    soma_idade += idade
    qtd_atletas += 1
    if sexo == 'M' and altura > float(atleta_mais_alto_masculino[3]):
        atleta_mais_alto_masculino = nome
    elif sexo == 'F' and peso > float(atleta_mais_pesada_feminino[3]):
        atleta_mais_pesada_feminino = nome
    if idade < float(atleta_mais_jovem[3]):
        atleta_mais_jovem = nome

media_idade = soma_idade / qtd_atletas

print(f'O atleta do sexo masculino mais alto é {atleta_mais_alto_masculino}')
print(f'A atleta do sexo feminino mais pesada é {atleta_mais_pesada_feminino}')
print(f'A média de idade dos atletas é {media_idade}')
print(f'O atleta mais jovem é {atleta_mais_jovem}')

