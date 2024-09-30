```
idade = []
while True:
    x = input("Insira a idade da pessoa (ou 'fim' para parar): ")
    if x.lower() == 'fim':
        break
    idade.append(int(x))

pessoas_menores = 0
pessoas_maiores = 0

for i in idade:
    if i < 21:
        pessoas_menores += 1
    elif i > 50:
        pessoas_maiores += 1

print(f"Pessoas com menos de 21 anos: {pessoas_menores}")
print(f"Pessoas com mais de 50 anos: {pessoas_maiores}")

