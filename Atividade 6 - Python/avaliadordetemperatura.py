def soma_digitos(numero):
    if not numero.isdigit():
        return "Valor informado é inválido! Por favor, forneça um número inteiro."
    return sum(int(digit) for digit in numero)

def calcular_temperaturas(temp_min, temp_max):
    # Calcula a média das temperaturas
    media = (temp_min + temp_max) / 2
    # Calcula a variação entre as temperaturas
    variacao = temp_max - temp_min
    return media, variacao

try:
    temp_min = float(input("Digite a temperatura mínima: "))
    temp_max = float(input("Digite a temperatura máxima: "))
    
    media, variacao = calcular_temperaturas(temp_min, temp_max)
    
    print(f"Média entre as temperaturas: {media:.2f}")
    print(f"Variação entre as temperaturas: {variacao:.2f}")
    
except ValueError:
    print("Valor informado é inválido! Por favor, forneça valores numéricos válidos para as temperaturas.")

numero_str = input("Digite um número para somar seus dígitos: ")

resultado_soma_digitos = soma_digitos(numero_str)
print(resultado_soma_digitos)
