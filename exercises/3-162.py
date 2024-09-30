```
def mmc(a, b):
    maior = max(a, b)
    menor = min(a, b)
    mmc = menor
    while True:
        if mmc % maior == 0 and mmc % menor == 0:
            return mmc
        mmc += 1
a = int(input("Insira o primeiro número: "))
b = int(input("Insira o segundo número: "))
print("O M.M.C. entre", a, "e", b, "é", mmc(a, b))

