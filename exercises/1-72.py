peso = int(input())
peso_gramas = peso * 1000
engordar = peso_gramas * 0.12
novo_peso_gramas = peso_gramas + engordar
novo_peso = (engordar / peso_gramas) * 100
print(f"Peso em gramas: {peso_gramas}")
print(f"Novo peso (engordar 12%): {novo_peso_gramas}")
print(f"Novo peso (% de engorda): {novo_peso:.2f}%")

