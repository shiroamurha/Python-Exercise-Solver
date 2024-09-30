respostas = []
for i in range(5):
    pergunta = input(f"{['Telefonou', 'Esteve', 'Mora', 'Devia', 'Já trabalhou'][i]} para a vítima? ")
    respostas.append(pergunta.lower() == 'sim')

print(respostas)

