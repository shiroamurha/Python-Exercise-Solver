altura = []
for i in range(6):
    h = float(input("Insira a altura da pessoa {}: ".format(i+1)))
    altura.append(h)
print("A maior altura é {} e a menor é {}".format(max(altura), min(altura)))

