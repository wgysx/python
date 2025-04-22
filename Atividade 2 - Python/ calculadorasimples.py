num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Soma
soma = num1 + num2
print(f"Soma: {num1} + {num2} = {soma}")

# Subtração
subtracao = num1 - num2
print(f"Subtração: {num1} - {num2} = {subtracao}")

# Multiplicação
multiplicacao = num1 * num2
print(f"Multiplicação: {num1} x {num2} = {multiplicacao}")

# Divisão
if num2 != 0:
    divisao = num1 / num2
    print(f"Divisão: {num1} ÷ {num2} = {divisao}")
else:
    print("Divisão: Não é possível dividir por zero.")
