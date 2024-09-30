```
diaria_normal = float(input())
taxa_promocao = 0.22
ocupacao_media_sem_promocao = 0.4
ocupacao_esperada = 0.7

diaria_promocao = diaria_normal * (1 - taxa_promocao)
valor_mensal_sem_promocao = diaria_normal * 42 * ocupacao_media_sem_promocao
valor_mensal_com_promocao = diaria_promocao * 42 * ocupacao_esperada
lucro_mensal = valor_mensal_com_promocao - valor_mensal_sem_promocao

print(f"Valor da diária no período da promoção: R$ {diaria_promocao:.2f}")
print(f"Valor médio arrecadado sem a promoção, durante um mês: R$ {valor_mensal_sem_promocao:.2f}")
print(f"Valor médio arrecadado com a promoção, durante um mês: R$ {valor_mensal_com_promocao:.2f}")
print(f"Lucro ou prejuízo mensal com a promoção: R$ {lucro_mensal:.2f}")
```

