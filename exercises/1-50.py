ano = int(input("Insira a idade em anos: "))
meses = int(input("Insira a idade em meses: "))
dias = int(input("Insira a idade em dias: "))

dias_total = (ano * 365) + (meses * 30) + dias

print(f"A idade é igual a {dias_total} dias.")

