entrada = input("Digite um número inteiro: ")

try:
    numero = int(entrada)
    if numero % 2 == 0:
        print(True)   # É par
    else:
        print(False)  # É ímpar
except ValueError:
    print("Valor inválido! Por favor, digite um número inteiro.")
