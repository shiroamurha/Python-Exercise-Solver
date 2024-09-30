```
a = float(input("Insira o valor do primeiro lado: "))
b = float(input("Insira o valor do segundo lado: "))
c = float(input("Insira o valor do terceiro lado: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Valor inválido. Nenhum dos lados pode ser igual a zero.")
else:
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print("O triângulo é eqüilátero.")
        elif a == b or a == c or b == c:
            print("O triângulo é isósceles.")
        else:
            print("O triângulo é escaleno.")
    else:
        print("Os valores não formam um triângulo.")

