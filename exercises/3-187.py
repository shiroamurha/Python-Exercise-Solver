```
ano_nasc = []
sexo = []
registro = []

while True:
    try:
        a = int(input("Ano de nascimento: "))
        s = input("Sexo (M/F): ")
        r = int(input("Item código de registro (1/0): "))
        ano_nasc.append(a)
        sexo.append(s)
        registro.append(r)
    except:
        break

menos_25_homem = len([x for x in range(len(ano_nasc)) if ano_nasc[x] < 25 and sexo[x] == 'M'])
menos_25_mulher = len([x for x in range(len(ano_nasc)) if ano_nasc[x] < 25 and sexo[x] == 'F'])
homem_fora_rs = len([x for x in range(len(registro)) if sexo[x] == 'M' and registro[x] == 0])

menos_25_homem_pct = (menos_25_homem / len([x for x in range(len(ano_nasc)) if sexo[x] == 'M'])) * 100
menos_25_mulher_pct = (menos_25_mulher / len([x for x in range(len(ano_nasc)) if sexo[x] == 'F'])) * 100
mulher_pct = (len([x for x in range(len(sexo)) if sexo[x] == 'F']) / len(sexo)) * 100
homem_fora_rs_pct = (homem_fora_rs / len([x for x in range(len(registro)) if sexo[x] == 'M'])) * 100

print(f"a) Porcentagem de motoristas homens com menos de 25 anos: {menos_25_homem_pct}%")
print(f"b) Porcentagem de mulheres: {mulher_pct}%")
print(f"c) Porcentagem de homens com registro fora do RS: {homem_fora_rs_pct}%")
print(f"d) Condição de parada: Ano de nascimento igual a zero: {'Sim' if 0 in ano_nasc else 'Não'}")

