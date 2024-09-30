```
cidades = [
    {"codigo": 1, "estado": "RS", "veiculos": 10000, "acidentes": 50},
    {"codigo": 2, "estado": "SC", "veiculos": 8000, "acidentes": 30},
    {"codigo": 3, "estado": "PR", "veiculos": 12000, "acidentes": 70},
    # ...
]

max_acidentes = max(cidades, key=lambda x: x["acidentes"])
min_acidentes = min(cidades, key=lambda x: x["acidentes"])

media_veiculos = sum(cidade["veiculos"] for cidade in cidades) / len(cidades)

media_acidentes_rgs = sum(cidade["acidentes"] for cidade in cidades if cidade["estado"] == "RS") / len([cidade for cidade in cidades if cidade["estado"] == "RS"])

print("a) Cidade com mais acidentes:", max_acidentes["codigo"], "(", max_acidentes["acidentes"], ")")
print("Cidade com menos acidentes:", min_acidentes["codigo"], "(", min_acidentes["acidentes"], ")")

print("b) Média de veículos:", media_veiculos)

print("c) Média de acidentes com vítimas no RS:", media_acidentes_rgs)

