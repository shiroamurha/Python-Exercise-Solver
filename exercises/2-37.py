```
nome = input("Digite seu nome: ")
escolha = int(input("Escolha um símbolo (1 - pedra, 2 - tesoura, 3 - papel): "))

from random import randint
computador = randint(1, 3)

if escolha == 1:
    escolha_usuario = "pedra"
elif escolha == 2:
    escolha_usuario = "tesoura"
elif escolha == 3:
    escolha_usuario = "papel"

if computador == 1:
    escolha_computador = "pedra"
elif computador == 2:
    escolha_computador = "tesoura"
elif computador == 3:
    escolha_computador = "papel"

print(f"{nome} escolheu {escolha_usuario} e o computador {escolha_computador}")

if escolha == computador:
    print("Empate!")
elif (escolha == 1 and computador == 2) or (escolha == 2 and computador == 3) or (escolha == 3 and computador == 1):
    print(f"{nome} ganhou!")
else:
    print(f" Computador ganhou!")

