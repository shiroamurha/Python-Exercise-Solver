```
idades = []
pesos = []

for i in range(int(input("Digite o número de pessoas: "))):
    idade = int(input(f"Idade da pessoa {i+1}: "))
    idade = int(input(f"Peso da pessoa {i+1}: "))
    idades.append(idade)
    pesos.append(idade)

maior_idade = max(idades)
media_idade = sum(idades) / len(idades)
pessoas_90kg = sum(1 for peso in pesos if peso > 90)
pessoas_15_50 = sum(1 for idade in idades if 15 <= idade <= 50)
pessoas_menos_18 = sum(1 for idade in idades if idade < 18)
media_peso_50 = sum(peso for idade, peso in zip(idades, pesos) if idade > 50) / sum(1 for idade in idades if idade > 50)

print(f"a) {pessoas_90kg} pessoas com mais de 90kg")
print(f"b) Média das idades: {media_idade}")
print(f"c) Maior idade: {maior_idade}")
print(f"d) {pessoas_15_50} pessoas com idade entre 15 e 50 anos")
print(f"e) {pessoas_menos_18} pessoas com menos de 18 anos")
print(f"f) Média de peso das pessoas com idade superior a 50 anos: {media_peso_50}")
```

