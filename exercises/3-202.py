```
fazendas = {}
total_manadas = 0
total_cabecas = 0
while True:
    codigo_fazenda = int(input())
    if codigo_fazenda == -1:
        break
    if codigo_fazenda not in fazendas:
        fazendas[codigo_fazenda] = {}
    while True:
        codigo_manada = int(input())
        if codigo_manada == -1:
            break
        tipo_manada = int(input())
        quantidade = int(input())
        if tipo_manada not in fazendas[codigo_fazenda]:
            fazendas[codigo_fazenda][tipo_manada] = 0
        fazendas[codigo_fazenda][tipo_manada] += quantidade
        total_cabecas += quantidade
        total_manadas += 1
    for tipo_manada in fazendas[codigo_fazenda]:
        print(f"Código da fazenda: {codigo_fazenda}, Tipo da manada: {tipo_manada}, Total de cabeças: {fazendas[codigo_fazenda][tipo_manada]}")
    print(f"Total de manadas da fazenda: {len(fazendas[codigo_fazenda])}")
for tipo_manada in set([manada for fazenda in fazendas.values() for manada in fazenda]):
    print(f"Total de cabeças do tipo {tipo_manada}: {sum([fazenda[tipo_manada] for fazenda in fazendas.values() if tipo_manada in fazenda])}")
print(f"Total de manadas da associação: {total_manadas}")
print(f"Total de cabeças da associação: {total_cabecas}")
```

