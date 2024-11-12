# Faturamento por estado
faturamento_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Calcular o faturamento total
faturamento_total = sum(faturamento_estado.values())

# Calcular o percentual de cada estado
for estado, faturamento in faturamento_estado.items():
    percentual = (faturamento / faturamento_total) * 100
    print(f"Percentual de {estado}: {percentual:.2f}%")