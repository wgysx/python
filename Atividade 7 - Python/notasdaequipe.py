def calcular_notas():
    notas = []  # Lista para armazenar as notas
    
    # Coleta as 5 notas
    for i in range(1, 6):
        while True:
            try:
                nota = float(input(f"Digite a nota do aluno {i}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Nota inválida! As notas devem ser entre 0 e 10.")
            except ValueError:
                print("Valor inválido! Por favor, insira um número válido.")
    
    maior_nota = max(notas)
    menor_nota = min(notas)
    media = sum(notas) / len(notas)
    
    print(f"\nMaior nota: {maior_nota}")
    print(f"Menor nota: {menor_nota}")
    print(f"Média das notas: {media:.2f}")

calcular_notas()
