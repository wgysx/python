def soma_digitos(numero):
    # Verifica se o número é um inteiro
    if numero.isdigit():
        # Soma os dígitos do número
        return sum(int(digit) for digit in numero)
    else:
        return "Valor informado não é um número inteiro!"

numero_usuario = input("Digite um número inteiro: ")

resultado = soma_digitos(numero_usuario)

print(resultado)
