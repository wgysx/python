def forma_triangulo(a, b, c):
    # Verifica a condição dos lados
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False

lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

print(forma_triangulo(lado1, lado2, lado3))
