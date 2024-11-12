def inverter_string(s):
    invertida = ''
    for i in range(len(s)-1, -1, -1):
        invertida += s[i]
    return invertida

# Exemplo de uso
texto = input("Informe uma string: ")
texto_invertido = inverter_string(texto)
print(f"A string invertida é: {texto_invertido}")