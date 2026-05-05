import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def carregar_dados():
    try:
        df = pd.read_csv('ninjas.csv')
        # Limpa espaços extras nos nomes das colunas e dados
        df.columns = df.columns.str.strip()
        return df
    except FileNotFoundError:
        print("Erro: O arquivo 'ninjas.csv' não foi encontrado na pasta.")
        return None

def gerar_radar(df, nomes_selecionados):
    categorias = ['Ninjutsu', 'Taijutsu', 'Genjutsu', 'Inteligencia', 'Forca', 'Velocidade']
    num_vars = len(categorias)
    
    # Configuração dos ângulos para o radar
    angulos = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angulos += angulos[:1]

    fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

    for nome in nomes_selecionados:
        # Filtra o ninja no DataFrame
        dados_ninja = df[df['Nome'] == nome]
        
        if not dados_ninja.empty:
            # Extrai valores e a cor
            valores = dados_ninja[categorias].values.flatten().tolist()
            cor = dados_ninja['Cor'].values[0]
            
            # Fecha o círculo do gráfico
            valores += valores[:1]
            
            ax.plot(angulos, valores, color=cor, linewidth=2, label=nome)
            ax.fill(angulos, valores, color=cor, alpha=0.15)
        else:
            print(f"Ninja '{nome}' não encontrado.")

    # Estilização técnica do gráfico
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_xticks(angulos[:-1])
    ax.set_xticklabels(categorias, size=12, fontweight='bold', color='#4B0082')
    ax.set_ylim(0, 5)
    
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    plt.title('BYAKUGAN: Análise de Chakra Comparativa', size=18, color='#4B0082', pad=30)
    plt.show()

def menu_principal():
    df = carregar_dados()
    if df is None: return

    while True:
        print("\n--- SISTEMA DE ANÁLISE HYUGA ---")
        print("1. Listar todos os Ninjas")
        print("2. Filtrar Ninjas por Vila")
        print("3. Comparar Ninjas específicos")
        print("4. Sair")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            print("\n", df[['Nome', 'Vila']])
        
        elif opcao == '2':
            vila = input("Digite a Vila (ex: Konoha, Suna, Akatsuki): ")
            ninjas_vila = df[df['Vila'].str.lower() == vila.lower()]
            if not ninjas_vila.empty:
                print(f"\nNinjas de {vila}:")
                print(ninjas_vila[['Nome']])
                if input("Deseja gerar gráfico desta Vila? (s/n): ").lower() == 's':
                    gerar_radar(df, ninjas_vila['Nome'].tolist())
            else:
                print("Nenhum ninja encontrado para esta vila.")

        elif opcao == '3':
            print("Disponíveis:", ", ".join(df['Nome'].tolist()))
            escolha = input("Digite os nomes separados por vírgula: ").split(',')
            nomes = [n.strip() for n in escolha]
            gerar_radar(df, nomes)

        elif opcao == '4':
            print("Desativando Byakugan... Até logo!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu_principal()