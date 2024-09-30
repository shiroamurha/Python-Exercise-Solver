```
qtd_livros = float(input("Digite a quantidade de livros: "))
desconto_a = 0.25 * qtd_livros + 7.50
desconto_b = 0.50 * qtd_livros + 2.50

if desconto_a < desconto_b:
    print(f"O critério A é o mais vantajoso: R$0,25 por livro + R$7,50 fixo")
    print(f"Total: R${desconto_a:.2f}")
    print(f"O critério B é o segundo mais vantajoso: R$0,50 por livro + R$2,50 fixo")
    print(f"Total: R${desconto_b:.2f}")
elif desconto_b < desconto_a:
    print(f"O critério B é o mais vantajoso: R$0,50 por livro + R$2,50 fixo")
    print(f"Total: R${desconto_b:.2f}")
    print(f"O critério A é o segundo mais vantajoso: R$0,25 por livro + R$7,50 fixo")
    print(f"Total: R${desconto_a:.2f}")
else:
    print("Os dois critérios deram o mesmo desconto")
    print(f"O critério A: R$0,25 por livro + R$7,50 fixo")
    print(f"Total: R${desconto_a:.2f}")
    print(f"O critério B: R$0,50 por livro + R$2,50 fixo")
    print(f"Total: R${desconto_b:.2f}")

