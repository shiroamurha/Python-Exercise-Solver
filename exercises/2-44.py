```
from datetime import datetime

def idade():
    nascimento = input("Insira a data de nascimento (dd/mm/aaaa): ")
    dia, mes, ano = map(int, nascimento.split('/'))
    nascimento = datetime(ano, mes, dia)
    idade = datetime.now().year - nascimento.year
    if (datetime.now().month, datetime.now().day) < (mes, dia):
        idade -= 1
    if idade > 50:
        print("Já tem mais de 50 anos.")
    else:
        print(f"Faltam {50-idade} anos para chegar aos 50 anos.")

def calculadora():
    num1 = float(input("Insira o primeiro valor: "))
    operacao = input("Insira a operação (+, -, *, /): ")
    num2 = float(input("Insira o segundo valor: "))
    
    if operacao == "+":
        print(num1 + num2)
    elif operacao == "-":
        print(num1 - num2)
    elif operacao == "*":
        print(num1 * num2)
    elif operacao == "/":
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Não é possível dividir por zero!")
    else:
        print("Operação inválida!")

idade()
calculadora()

