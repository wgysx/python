import random

def jogo_adivinhacao():
    # Gera um número aleatório entre 1 e 100
    numero_gerado = random.randint(1, 100)
    
    tentativas = 0  
    acerto = False  
    
   
    while not acerto:
        try:
            palpite = int(input("Adivinhe o número (entre 1 e 100): "))
            tentativas += 1  
            
            if palpite < numero_gerado:
                print("O número é maior! Tente novamente.")
            elif palpite > numero_gerado:
                print("O número é menor! Tente novamente.")
            else:
                acerto = True  
                print(f"Parabéns! Você acertou o número {numero_gerado} em {tentativas} tentativas.")
        
        except ValueError:
            print("Por favor, insira um número válido.")

jogo_adivinhacao()
