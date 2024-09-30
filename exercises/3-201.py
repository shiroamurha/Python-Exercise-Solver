```
print("MENU do PROGRAMA")
print("1. Lê dez palavras e mostra a menor delas")
print("2. Lê uma palavra e armazena a letra W em todas as posições pares da palavra")
print("3. Lê uma frase e exibe o número de palavras existentes na frase")
print("4. Lê uma palavra e retorna quantas vogais existem")
print("5. Lê uma frase e mostra o comprimento")
print("6. Lê uma palavra e mostra ela invertida")
print("7. Lê 3 nomes e mostra o maior")
print("8. Lê uma frase e substitui todas as vogais por X e mostra")
print("9. Lê uma frase e retorna o número de vogais, de consoantes e de palavras")
print("10. Sair do Programa")
opcao = int(input("ESCOLHA A OPÇÃO: "))

if opcao == 1:
    palavras = input("Entre com 10 palavras: ").split()
    print("A menor palavra é: ", min(palavras))

elif opcao == 2:
    palavra = input("Entre com uma palavra: ")
    palavra = list(palavra)
    for i in range(0, len(palavra), 2):
        palavra[i] = 'W'
    print(''.join(palavra))

elif opcao == 3:
    frase = input("Entre com uma frase: ").split()
    print("O número de palavras é: ", len(frase))

elif opcao == 4:
    palavra = input("Entre com uma palavra: ")
    vogais = 'aeiouAEIOU'
    count = 0
    for letra in palavra:
        if letra in vogais:
            count += 1
    print("A palavra tem ", count, " vogais")

elif opcao == 5:
    frase = input("Entre com uma frase: ")
    print("O comprimento da frase é: ", len(frase))

elif opcao == 6:
    palavra = input("Entre com uma palavra: ")
    print("A palavra invertida é: ", palavra[::-1])

elif opcao == 7:
    nomes = input("Entre com 3 nomes: ").split()
    print("O maior nome é: ", max(nomes))

elif opcao == 8:
    frase = input("Entre com uma frase: ")
    vogais = 'aeiouAEIOU'
    for i in range(len(frase)):
        if frase[i] in vogais:
            frase = frase.replace(frase[i], 'X')
    print(frase)

elif opcao == 9:
    frase = input("Entre com uma frase: ")
    vogais = 'aeiouAEIOU'
    count_vogais = 0
    count_consoantes = 0
    palavras = frase.split()
    for palavra in palavras:
        for letra in palavra:
            if letra in vogais:
                count_vogais += 1
            else:
                count_consoantes += 1
    print("O número de vogais é: ", count_vogais)
    print("O número de consoantes é: ", count_consoantes)
    print("O número de palavras é: ", len(palavras))

elif opcao == 10:
    print("Saindo do programa...")

else:
    print("Opção inválida")

