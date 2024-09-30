```
nome = ''
sexo = ''
idade = 0
experiencia = False
escolaridade = ''
total_feminino = 0
total_masculino = 0
total_graduacao = 0
total_experiencia = 0
homem_35_45 = 0
idade_minima_mulher = 0
idade_jovem_psg = 0
total_fundamental_ou_medio = 0
total_experiencia_mais_30 = 0

while True:
    nome = input("Nome: ")
    sexo = input("Sexo (feminino/masculino): ")
    idade = int(input("Idade: "))
    experiencia = input("Experiência (sim/não): ") == "sim"
    escolaridade = input("Escolaridade (ensino Fundamental/ensino Médio/Graduação/Pós-graduação): ")

    if sexo == "feminino":
        total_feminino += 1
    else:
        total_masculino += 1
        if idade > 21:
            total_masculino += 1
    if escolaridade == "Graduação":
        total_graduacao += 1
    if experiencia:
        total_experiencia += 1
        if idade > 30:
            total_experiencia_mais_30 += 1
    if sexo == "feminino" and experiencia:
        total_experiencia += 1
    if sexo == "masculino" and idade >= 35 and idade <= 45:
        homem_35_45 += 1
    if sexo == "feminino" and experiencia and idade < idade_minima_mulher:
        idade_minima_mulher = idade
    if sexo == "feminino" and experiencia and idade < idade_jovem_psg:
        idade_jovem_psg = idade
    if sexo == "masculino" and idade < idade_jovem_psg:
        idade_jovem_psg = idade
    if sexo == "feminino" and escolaridade == "ensino Fundamental" or escolaridade == "ensino Médio" and idade < 21:
        total_fundamental_ou_medio += 1

    resposta = input("Deseja cadastrar outro candidato? (sim/não): ")
    if resposta == "não":
        break

print("a) Número de candidatos do sexo feminino:", total_feminino)
print("b) Número de candidatos do sexo masculino com mais de 21 anos:", total_masculino)
print("c) Idade média dos homens com escolaridade Graduação:", total_graduacao / total_masculino)
print("d) Idade média das mulheres com experiência:", total_experiencia / total_feminino)
print("e) Total de candidatos com escolaridade Graduação:", total_graduacao)
print("f) Porcentagem dos homens entre 35 e 45 anos entre o total dos homens cadastrados:", (homem_35_45 / total_masculino) * 100)
print("g) Menor idade entre as mulheres que já têm experiência no serviço:", idade_minima_mulher)
print("h) Total de candidatos com escolaridade ensino Fundamental ou ensino Médio que tenham menos de 21 anos:", total_fundamental_ou_medio)
print("i) Quantidade de candidatos com experiência no serviço e que tenham mais de 30 anos:", total_experiencia_mais_30)
print("j) Idade do candidato mais jovem e que ja possui Pós graduação:", idade_jovem_psg)

