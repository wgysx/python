operacao = input("Qual operação deseja realizar? (soma, subtracao, multiplicacao, divisao): ").lower()

# Verifica se a operação é válida
if operacao not in ['soma', 'subtracao', 'multiplicacao', 'divisao']:
    print("Operação inválida! Por favor, escolha entre: soma, subtracao, multiplicacao ou divisao.")
else:
    # Solicita os dois números
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Realiza a operação escolhida
    if operacao == 'soma':
        resultado = num1 + num2
        print(f"Resultado da soma: {resultado}")

    elif operacao == 'subtracao':
        resultado = num1 - num2
        print(f"Resultado da subtração: {resultado}")

    elif operacao == 'multiplicacao':
        resultado = num1 * num2
        print(f"Resultado da multiplicação: {resultado}")

    elif operacao == 'divisao':
        if num2 != 0:
            resultado = num1 / num2
            print(f"Resultado da divisão: {resultado}")
        else:
            print("Não é possível dividir por zero.")
