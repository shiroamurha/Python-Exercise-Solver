```
import math

def soma_valores():
    valores = []
    quantidade = int(input("Quantos valores você deseja somar? "))
    for i in range(quantidade):
        valores.append(float(input(f"Digite o {i+1}º valor: ")))
    print(f"A soma dos valores é: {sum(valores)}")

def subtracao_valores():
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    print(f"A subtração dos valores é: {valor1 - valor2}")

def baskara():
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    delta = b**2 - 4*a*c
    if delta < 0:
        print("A equação não tem raízes reais.")
    elif delta == 0:
        print("A equação tem uma raiz real.")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"A raiz 1 é: {raiz1} e a raiz 2 é: {raiz2}")

def media_aritmetica():
    valores = []
    quantidade = int(input("Quantos valores você deseja calcular a média? "))
    for i in range(quantidade):
        valores.append(float(input(f"Digite o {i+1}º valor: ")))
    print(f"A média dos valores é: {sum(valores) / len(valores)}")

def media_ponderada():
    valores = []
    pesos = []
    quantidade = int(input("Quantos valores você deseja calcular a média ponderada? "))
    for i in range(quantidade):
        valores.append(float(input(f"Digite o {i+1}º valor: ")))
        pesos.append(float(input(f"Digite o peso do {i+1}º valor: ")))
    print(f"A média ponderada dos valores é: {sum([valor*peso for valor, peso in zip(valores, pesos)]) / sum(pesos)}")

def potencia():
    valor = float(input("Digite o valor base: "))
    expoente = float(input("Digite o expoente: "))
    print(f"A potência é: {valor**expoente}")

def funcao_f():
    x = float(input("Digite o valor de x: "))
    print(f"A função é: {5*x}")

def funcao_x2():
    x = float(input("Digite o valor de x: "))
    print(f"A função é: {x**2 - 5}")

def funcao_xy():
    x = float(input("Digite o valor de x: "))
    y = float(input("Digite o valor de y: "))
    print(f"A função é: {x**3 - 2*y - 2}")

def main():
    while True:
        print("1. Soma valores")
        print("2. Subtração de 2 valores")
        print("3. Baskara")
        print("4. Média aritmética")
        print("5. Média ponderada")
        print("6. Potência")
        print("7. f(x) = 5x")
        print("8. f(x) = x2 - 5")
        print("9. f(x, y) = x3 - 2y - 2")
        print("10. Sair")
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            soma_valores()
        elif opcao == 2:
            subtracao_valores()
        elif opcao == 3:
            baskara()
        elif opcao == 4:
            media_aritmetica()
        elif opcao == 5:
            media_ponderada()
        elif opcao == 6:
            potencia()
        elif opcao == 7:
            funcao_f()
        elif opcao == 8:
            funcao_x2()
        elif opcao == 9:
            funcao_xy()
        elif opcao == 10:
            print("Finalizando...")
            break
        else:
            print("Opção inválida. Tente novamente.")
        continuar = input("Deseja digitar outra opção? (s/n) ")
        if continuar.lower() != "s":
            print("Finalizando...")
            break

if __name__ == "__main__":
    main()

