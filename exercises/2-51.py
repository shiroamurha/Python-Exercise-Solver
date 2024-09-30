```
def questao55():
    salario = float(input("Insira o salário: "))
    tempo_trabalho = int(input("Insira o tempo de trabalho: "))
    if tempo_trabalho >= 5:
        bônus = salario * 0.20
    else:
        bônus = salario * 0.10
    print("O valor do bônus é: R$%.2f" % bônus)

def questao56():
    quantidade_livros = int(input("Insira a quantidade de livros: "))
    valor_desconto_a = quantidade_livros * 0.25 + 7.50
    valor_desconto_b = quantidade_livros * 0.50 + 2.50
    if valor_desconto_a < valor_desconto_b:
        print("A melhor opção é o critério A")
    elif valor_desconto_a > valor_desconto_b:
        print("A melhor opção é o critério B")
    else:
        print("Ambas as opções são iguais")
```

