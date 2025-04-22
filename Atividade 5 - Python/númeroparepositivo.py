def verifica_par_e_positivo(numero):
    # Verifica se o número é par e positivo
    if numero > 0 and numero % 2 == 0:
        return True
    else:
        return False

numero_usuario = float(input("Digite um número: "))

print(verifica_par_e_positivo(numero_usuario))
