idade_input = input("Digite sua idade: ")

try:
    idade = int(idade_input)
    
    if idade < 0:
        print("Valor inválido! A idade não pode ser negativa.")
    elif idade < 18:
        print("Você é menor de idade.")
    elif idade < 60:
        print("Você é adulto.")
    else:
        print("Você é idoso.")
except ValueError:
    print("Valor inválido! Por favor, digite um número inteiro.")
