```
cc = float(input())
pp = float(input())

if cc > 1000 or pp > 1000:
    if cc > pp:
        limite = cc * 2
    else:
        limite = pp * 3
    print(f'O limite da conta especial é R$ {limite:.2f}')
else:
    print('SEM CONTA ESPECIAL')

