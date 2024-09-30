```
qtd_dvds = int(input())
valor_aluguel = float(input())

dvds_alugados = qtd_dvds // 3
faturamento_anual = dvds_alugados * valor_aluguel * 12

dvds_atrasados = dvds_alugados // 10
valor_multas = dvds_atrasados * valor_aluguel * 0.1

dvds_estragados = qtd_dvds * 0.02
dvds_comprados = qtd_dvds * 0.1

qtd_dvds_final = qtd_dvds - dvds_estragados + dvds_comprados

print(f"Faturamento anual: R$ {faturamento_anual:.2f}")
print(f"Valor ganho com multas: R$ {valor_multas:.2f}")
print(f"Quantidade de DVDs no final do ano: {int(qtd_dvds_final)}")
```

