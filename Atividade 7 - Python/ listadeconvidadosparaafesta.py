def lista_convidados():
    convidados = []  # Lista para armazenar os nomes dos convidados
    
    # Coleta de 6 nomes de convidados
    for i in range(1, 7):
        nome = input(f"Digite o nome do convidado {i}: ")
        convidados.append(nome)
    
    convidados_unicos = list(set(convidados))
    
    convidados_unicos.sort()
    
    print(f"\nLista final de convidados (sem duplicatas e ordenada): {convidados_unicos}")

lista_convidados()
