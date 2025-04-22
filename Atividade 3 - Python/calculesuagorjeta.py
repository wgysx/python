def dolares_para_float(d):
    # Remove o símbolo de dólar e converte para float
    return float(d.replace('$', ''))

def percentual_para_float(p):
    # Remove o símbolo de porcentagem e converte para decimal
    return float(p.replace('%', '')) / 100

dolares = dolares_para_float(input("Quanto custou a refeição? "))        # Ex: $50.00
percentual = percentual_para_float(input("Qual percentual você gostaria de deixar de gorjeta? "))  # Ex: 15%

# Calcula a gorjeta
gorjeta = dolares * percentual

print(f"Deixe ${gorjeta:.2f}")
