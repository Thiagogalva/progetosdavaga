import json

# Exemplo de faturamento diário em formato JSON
faturamento_diario = """
{
    "faturamento": [
        {"dia": 1, "valor": 500},
        {"dia": 2, "valor": 1000},
        {"dia": 3, "valor": 1500},
        {"dia": 4, "valor": 2000},
        {"dia": 5, "valor": 0},
        {"dia": 6, "valor": 1500},
        {"dia": 7, "valor": 200},
        {"dia": 8, "valor": 1800}
    ]
}
"""

# Carregar o JSON
dados = json.loads(faturamento_diario)
faturamento = [item["valor"] for item in dados["faturamento"]]

# Remover valores de faturamento 0 (dias sem faturamento)
faturamento = [f for f in faturamento if f > 0]

# Calcular o menor e maior faturamento
menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)

# Calcular a média mensal
media_faturamento = sum(faturamento) / len(faturamento)

# Calcular número de dias com faturamento acima da média
dias_acima_media = len([f for f in faturamento if f > media_faturamento])

print(f"Menor faturamento: R${menor_faturamento:.2f}")
print(f"Maior faturamento: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento superior à média: {dias_acima_media}")