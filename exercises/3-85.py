altura = []
for i in range(10):
    alt = float(input("Insira a altura da {}ª pessoa: ".format(i+1)))
    altura.append(alt)
print("A maior altura é: ", max(altura))

