base = float(input("Insira a base do retângulo: "))
altura = float(input("Insira a altura do retângulo: "))

perimetro = 2 * (base + altura)
area = base * altura
diagonal = (base**2 + altura**2)**0.5

print("Perímetro:", perimetro)
print("Área:", area)
print("Diagonal:", diagonal)

