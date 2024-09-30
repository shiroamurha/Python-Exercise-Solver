```
n1 = float(input("Entre com o primeiro número: "))
n2 = float(input("Entre com o segundo número: "))

if n1 < n2:
    menor = n1
    maior = n2
else:
    menor = n2
    maior = n1

if maior < 0:
    print("A raiz quadrada de um número negativo não é um número real.")
else:
    print("O quadrado do menor número é: ", menor**2)
    print("A raiz quadrada do maior número é: ", maior**0.5)

