```
def calcular_area():
    print("1 - Quadrado")
    print("2 - Retângulo")
    print("3 - Círculo")
    print("4 - Trapézio")
    opcao = int(input("Selecione a opção: "))
    if opcao == 1:
        lado = float(input("Insira o lado do quadrado: "))
        area = lado ** 2
    elif opcao == 2:
        comprimento = float(input("Insira o comprimento do retângulo: "))
        largura = float(input("Insira a largura do retângulo: "))
        area = comprimento * largura
    elif opcao == 3:
        raio = float(input("Insira o raio do círculo: "))
        area = 3.14 * (raio ** 2)
    elif opcao == 4:
        base_maior = float(input("Insira a base maior do trapézio: "))
        base_menor = float(input("Insira a base menor do trapézio: "))
        altura = float(input("Insira a altura do trapézio: "))
        area = ((base_maior + base_menor) * altura) / 2
    print("A área é:", area)

def converter_moeda():
    print("1 - Euro")
    print("2 - Libra Esterlina")
    print("3 - Dólar")
    opcao = input("Selecione a opção: ")
    valor_real = float(input("Insira o valor em reais: "))
    if opcao == "1":
        valor_euro = valor_real / 5.5
        print("O valor em euros é: ", valor_euro)
    elif opcao == "l":
        valor_libra = valor_real / 0.8
        print("O valor em libras é: ", valor_libra)
    elif opcao == "d":
        valor_dolar = valor_real / 4.5
        print("O valor em dólares é: ", valor_dolar)

while True:
    print("1 - Calcular área")
    print("2 - Converter moeda")
    opcao = int(input("Selecione a opção: "))
    if opcao == 1:
        calcular_area()
    elif opcao == 2:
        converter_moeda()
    else:
        break

