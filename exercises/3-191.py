```
contas = []
while True:
    num_telefone = input()
    nome_cliente = input()
    tipo_linha = int(input())
    pulsos_fixo_fixo = float(input())
    pulsos_fixo_celular = float(input())
    ano_adesao = int(input())
    conta = float(pulsos_fixo_fixo * 0.5 + pulsos_fixo_celular * 0.7)
    if tipo_linha == 1:
        taxa_fixa = 20
    else:
        taxa_fixa = 30
    conta += taxa_fixa
    conta *= 1.25
    contas.append({'num_telefone': num_telefone, 'nome_cliente': nome_cliente, 'tipo_linha': tipo_linha, 'ano_adesao': ano_adesao, 'conta': conta, 'pulsos_fixo_fixo': pulsos_fixo_fixo, 'pulsos_fixo_celular': pulsos_fixo_celular})
    resposta = input()
    if resposta.lower() != 'sim':
        break

nome_cliente_residencial_mais_antigo = max(contas, key=lambda x: x['ano_adesao']).get('nome_cliente')
nome_cliente_comercial_maior_conta = max(contas, key=lambda x: x['conta' if x['tipo_linha'] == 2 else float('inf')]).get('nome_cliente')
total_arrecadado = sum(conta['conta'] for conta in contas)
total_icms = total_arrecadado * 0.25
total_pulsos_fixo_fixo = sum(conta['pulsos_fixo_fixo'] for conta in contas)

print(f"Nome do cliente residencial mais antigo: {nome_cliente_residencial_mais_antigo}")
print(f"Nome do cliente comercial com maior conta de telefone: {nome_cliente_comercial_maior_conta}")
print(f"Total arrecadado pela Empresa Tchau: {total_arrecadado}")
print(f"Total arrecadado de ICMS: {total_icms}")
print(f"Total de pulsos (fixo-fixo) por tipo de linha: {total_pulsos_fixo_fixo}")
```

