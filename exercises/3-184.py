```
n = int(input("Insira um número de 3 algarismos: "))
primeiro = n // 100
segundo = (n // 10) % 10
terceiro = n % 10
controle = (primeiro + segundo * 3 + terceiro * 5) % 7
novo_numero = int(str(n) + str(controle))
print(novo_numero)

# Questão 187
torcedores = {'Caxias': 0, 'Grêmio': 0, 'Inter': 0, 'Juventude': 0, 'Pelotas': 0, 'Xavante': 0}
moradores = {'Porto Alegre': 0, 'Canoas': 0, 'Esteio': 0, 'Sapucaia do Sul': 0, 'São Leopoldo': 0, 'Caxias': 0, 'Pelotas': 0}
salarios = []
while True:
    time_do_coracao = input("Qual o seu time do coração? (a) Caxias (b) Grêmio (c) Inter (d) Juventude (e) Pelotas (f) Xavante (g) Outros: ")
    mora = input("Onde você mora? (a) Porto Alegre (b) Canoas (c) Esteio (d) Sapucaia do Sul (e) São Leopoldo (f) Caxias (g) Pelotas: ")
    salario = float(input("Qual o seu salário? "))
    salarios.append(salario)
    torcedores[time_do_coracao] += 1
    moradores[mora] += 1
    resposta = input("Deseja continuar? (s) Sim (n) Não: ")
    if resposta.lower() != 's':
        break

print("a) Número de torcedores por clube:", torcedores)
print("b) Média dos salários dos torcedores do Inter e do Grêmio:", sum(salarios) / (torcedores['Inter'] + torcedores['Grêmio']))
print("c) Número de pessoas moradoras em Porto Alegre que não torcem pelo Grêmio e nem pelo Inter:", moradores['Porto Alegre'] - torcedores['Grêmio'] - torcedores['Inter'])
print("d) Número de pessoas que torcem pelo Xavante:", torcedores['Xavante'])
print("e) Total de pessoas entrevistadas:", sum(torcedores.values()))
print("f) Quantos torcedores tem salário entre R$ 1000 e R$ 3000:", sum(1 for salario in salarios if 1000 < salario < 3000))
print("g) Qual o time que tem mais torcedores que responderam a pesquisa:", max(torcedores, key=torcedores.get)
print("h) Maior salário:", max(salarios)
```

