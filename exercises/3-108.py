```
nome_clube = 1
quantidade_pessoas = 0
grêmio = 0
internacional = 0
outros = 0
porto_alegre = 0
outros_clubes = 0

while nome_clube != 0:
    nome_clube = int(input("Insira o número do clube (1-Grêmio; 2-Internacional; 3-Outros; 0-Fim): "))
    if nome_clube != 0:
        quantidade_pessoas += 1
        if nome_clube == 1:
            grêmio += 1
        elif nome_clube == 2:
            internacional += 1
        else:
            outros += 1
        cidade_origem = int(input("Insira a cidade de origem (0-Porto Alegre; 1-Outras): "))
        if cidade_origem == 0 and nome_clube > 2:
            outros_clubes += 1

print("Número de torcedores por clube:")
print("Grêmio:", grêmio)
print("Internacional:", internacional)
print("Outros:", outros)
print("Número de pessoas nascidas em Porto Alegre que não torcem por nenhum dos dois primeiros clubes:", outros_clubes)
print("Número de pessoas entrevistadas:", quantidade_pessoas)

