def calcular_media_notas():
    notas = []  # Lista para armazenar as notas
    
    # Coleta as 5 notas
    for i in range(1, 6):
        while True:
            try:
                nota = float(input(f"Digite a nota {i}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Nota inválida! As notas devem ser entre 0 e 10.")
            except ValueError:
                print("Valor inválido! Por favor, insira um número válido.")
    
    notas.sort()
    
    notas_validas = notas[1:-1]
    
    media = sum(notas_validas) / len(notas_validas)
    
    print(f"\nMédia das notas (descontando a maior e a menor): {media:.2f}")

calcular_media_notas()
