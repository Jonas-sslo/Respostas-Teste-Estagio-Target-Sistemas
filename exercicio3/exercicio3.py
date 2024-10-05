import json

valores = []
dias_com_faturamento_acima_da_media = []

with open("dados.json") as f:
    dados = json.load(f)

for dado in dados:
    if dado["valor"] != 0:
        valores.append(dado["valor"])
    else:
        valores.append(dado["valor"])

min_valor = min(valores)
min_valor_formatada = (f"{min_valor:.2f}")

max_valor = max(valores)
max_valor_formatada = (f"{max_valor:.2f}")

media_mensal = sum(valores) / len(dados)

for dado in dados:
        if dado["valor"] > media_mensal:
            dias_com_faturamento_acima_da_media.append(dado["dia"])

numero_dias_com_faturamento_acima_da_media = len(dias_com_faturamento_acima_da_media)




print(min_valor_formatada)
print(max_valor_formatada)
print(numero_dias_com_faturamento_acima_da_media)