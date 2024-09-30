```
v_total = 0
p_total = 0
total = 0
p_prestacao = 0

for i in range(15):
    codigo = input("Código da transação: ")
    valor = float(input("Valor da transação: "))
    
    if codigo == 'V':
        v_total += valor
    elif codigo == 'P':
        p_total += valor
        total += valor
        p_prestacao += valor / 3

print("a) Valor total das compras à vista:", v_total)
print("b) Valor total das compras a prazo:", p_total)
print("c) Valor total das compras efetuadas na loja:", total)
print("d) Valor da primeira prestação das compras a prazo:", p_prestacao)
```

