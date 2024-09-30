```
numeros = []
while True:
    num = int(input())
    if num == -1:
        break
    numeros.append(num)

if len([num for num in numeros if 100 < num < 1000]) > 0:
    maior_que_100_e_menor_que_1000 = [num for num in numeros if 100 < num < 1000]
    menor_valor = min(maior_que_100_e_menor_que_1000)
    media = sum(maior_que_100_e_menor_que_1000) / len(maior_que_100_e_menor_que_1000)
    soma = sum(maior_que_100_e_menor_que_1000)
    print(f"a) {miner_valor}")
    print(f"b) {media}")
    print(f"c) {soma}")
    print(f"d) {sum(numeros)}")
    print(f"e) {min(numeros)}")
    print(f"f) {max(numeros)}")
    print(f"g) {len(numeros)}")
else:
    print("Nenhum valor digitado está dentro do intervalo de 100 e 1000.")

votos = [0, 0, 0, 0, 0, 0]
for i in range(30):
    votos.append(int(input()))

print(f"a) Candidato 1: {votos[0]}")
print(f"b) Candidato 2: {votos[1]}")
print(f"c) Candidato 3: {votos[2]}")
print(f"d) Candidato 4: {votos[3]}")
print(f"e) Votos nulos: {votos[4]}")
print(f"f) Votos em branco: {votos[5]}")

total_votos = sum(votos[:4])
votos_nulos_brancos = sum(votos[4:])
porcentagem = (votos_nulos_brancos / total_votos) * 100
print(f"d) {porcentagem}%")

