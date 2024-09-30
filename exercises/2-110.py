```
saldo = float(input())
divida = float(input())

if divida > saldo:
    print("A divida não pode ser paga.")
elif divida <= 0.97 * saldo:
    print("Saldo suficiente para pagar em qualquer dia.")
elif divida <= 0.97 * saldo + 0.03 * divida:
    print("Saldo suficiente para pagar até o dia 20.")
else:
    print("Saldo suficiente para pagar até o dia 10.")
```

