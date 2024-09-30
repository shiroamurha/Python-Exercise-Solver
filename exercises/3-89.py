```
senha_correta = 2014
contador = 0
while True:
    senha = int(input("Digite a senha: "))
    contador += 1
    if senha == senha_correta:
        print("ACESSO PERMITIDO")
        print("Senha digitada", contador, "vezes")
        break
    else:
        print("SENHA INVÁLIDA")

