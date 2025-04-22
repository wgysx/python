def tipo_triangulo(a, b, c):
    # Verifica se os lados formam um triângulo válido
    if a + b > c and a + c > b and b + c > a:
        # Classifica o tipo de triângulo
        if a == b == c:
            return "Triângulo Equilátero"
        elif a == b or a == c or b == c:
            return "Triângulo Isósceles"
        else:
            return "Triângulo Escaleno"
    else:
        return "Os valores não formam um triângulo válido"

lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

# Verifica o tipo de triângulo ou se é inválido
resultado = tipo_triangulo(lado1, lado2, lado3)
print(resultado)
