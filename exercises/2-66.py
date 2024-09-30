```
nota_trabalho = float(input("Nota do trabalho: "))
nota_prova = float(input("Nota da prova: "))
nota_final = (0.25 * nota_trabalho) + (0.75 * nota_prova)
if nota_final < 7:
    print("Precisa de exame")
else:
    print(f"Passaste com {nota_final:.2f} de nota")

