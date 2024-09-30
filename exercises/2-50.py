```
verbo = input("Digite um verbo no infinitivo: ")
if verbo.endswith("ar"):
    print(f"{verbo} da 1a. Conjugação")
elif verbo.endswith("er"):
    print(f"{verbo} da 2a. Conjugação")
elif verbo.endswith("ir"):
    print(f"{verbo} da 3a. Conjugação")
else:
    print("Verbo não está no infinitivo")

