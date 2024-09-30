```
n = []
for i in range(12):
    n.append(float(input("Digite o %dº número: "%(i+1))))
media = sum(n) / len(n)
print("A média dos números é: %0.2f" % media)

