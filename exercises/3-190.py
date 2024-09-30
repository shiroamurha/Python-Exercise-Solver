```
idades = []
opinioes = []

while True:
    idade = int(input("Idade: "))
    opiniao = int(input("Opinião (10 ótimo, 7 bom, 5 regular, 3 ruim, 0 péssimo): "))
    idades.append(idade)
    opinioes.append(opiniao)
    if input("Deseja continuar? (s/n): ").lower() != 's':
        break

optimos = opinioes.count(10)
bomregular = opinioes.count(7) + opinioes.count(5)
ruim = opinioes.count(3)
pessimo = opinioes.count(0)

dif_bomregular = ((bomregular - ruim) / (bomregular + ruim)) * 100

media_ruim = sum([idade for idade, opiniao in zip(idades, opinioes) if opiniao == 3]) / ruim

pessimo_total = len([opiniao for opiniao in opinioes if opiniao == 0])
pessimo_maior_idade = max([idade for idade, opiniao in zip(idades, opinioes) if opiniao == 0])

print(f"a) Quantidade de respostas ótimo: {optimos}")
print(f"b) Diferença percentual entre respostas regular e bom: {dif_bomregular}%")
print(f"c) Média de idade das pessoas que responderam ruim: {media_ruim}")
print(f"d) Porcentagem de respostas péssimo: {pessimo_total / len(opinioes) * 100}%")
print(f"d) Maior idade que utilizou a opção péssimo: {pessimo_maior_idade}")
```

