```
def menor_combinacao(valor):
    notas = [200, 100, 50, 20, 10, 5, 2]
    moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
    resultado = []
    
    for nota in notas:
        quantidade = int(valor // nota)
        resultado.append((nota, quantidade))
        valor -= quantidade * nota
    
    for moeda in moedas:
        quantidade = int(valor // moeda)
        resultado.append((moeda, quantidade))
        valor -= quantidade * moeda
    
    return resultado

