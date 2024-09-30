```
def taxa_de_juros(tempo):
    if tempo >= 5:
        return 0.0095
    elif tempo >= 4:
        return 0.0090
    elif tempo >= 3:
        return 0.0085
    elif tempo >= 2:
        return 0.0075
    else:
        return 0.0065

