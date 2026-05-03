import time
import random

def iniciar_treino():
    golpes = ["Palma de Vácuo", "64 Palmas", "Punho dos Leões Gêmeos", "Agulha de Chakra", "Rotação", "Oito Trigramas"]
    pontuacao = 0
    tempo_limite = 3.0  # Segundos para cada golpe
    
    print("--- Treinamento do Clã Hyuga: Foco e Velocidade ---")
    print(f"Você tem {tempo_limite} segundos para cada golpe. Prepare seu Byakugan!\n")
    time.sleep(2)

    for i in range(1, 11):  # 10 rodadas de treino
        alvo = random.choice(golpes)
        print(f"Alvo {i}: {alvo}")
        
        inicio = time.time()
        entrada = input("Digite o golpe: ")
        fim = time.time()
        
        tempo_gasto = fim - inicio
        
        if entrada.lower() == alvo.lower() and tempo_gasto <= tempo_limite:
            print(f"✅ ACERTOU! Tempo: {tempo_gasto:.2f}s")
            pontuacao += 1
        elif tempo_gasto > tempo_limite:
            print(f"❌ MUITO LENTO! O alvo escapou ({tempo_gasto:.2f}s)")
        else:
            print(f"❌ ERROU A TÉCNICA!")
        print("-" * 30)

    print(f"\nTreino concluído! Precisão: {pontuacao}/10")
    if pontuacao == 10:
        print("Incrível! Você dominou os Oito Trigramas!")

if __name__ == "__main__":
    iniciar_treino()