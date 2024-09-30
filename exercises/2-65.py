```
import random

numero_secreto = random.randint(1, 100)
chances = 3

while chances > 0:
    chute = int(input("Chute um número entre 1 e 100: "))
    if chute == numero_secreto:
        print("Você acertou!")
        break
    elif chute < numero_secreto:
        print("O valor digitado é menor")
    else:
        print("O valor digitado é maior")
    chances -= 1
    print(f"Você tem {chances} chances restantes")
if chances == 0:
    print("Você perdeu! O número secreto era", numero_secreto)

