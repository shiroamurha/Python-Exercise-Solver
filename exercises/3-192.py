```
assinantes = []
while True:
    codigo = int(input())
    if codigo == 0:
        break
    tipo = input()
    pulsos = int(input())
    despertadores = int(input())
    tarifa = 23 if tipo == 'residencial' else 30
    conta = tarifa + (pulsos - 90) * 0.1 + despertadores * 0.47
    assinantes.append(conta)
    maior_conta = max(assinantes)
    assinante_maior_conta = [i for i, x in enumerate(assinantes) if x == maior_conta][0]
    media = sum(assinantes) / len(assinantes)
print(f'Total da conta do assinante {assinante_maior_conta + 1}: R${maior_conta:.2f}')
print(f'assinante que pagou a maior conta: {assinante_maior_conta + 1}')
print(f'Média arrecadada por assinante: R${media:.2f}')

