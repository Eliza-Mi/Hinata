import customtkinter as ctk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Configuração visual do tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class AppHyuga(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Análise Hyuga v3.0")
        self.geometry("900x600")
        
        # Carregar dados
        self.df = pd.read_csv('ninjas.csv')
        
        # Layout: Grid
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Barra Lateral (Menu)
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        self.label_titulo = ctk.CTkLabel(self.sidebar, text="BYAKUGAN VIEW", font=ctk.CTkFont(size=20, weight="bold"))
        self.label_titulo.pack(padx=20, pady=20)

        self.label_instrucao = ctk.CTkLabel(self.sidebar, text="Selecione os Ninjas:")
        self.label_instrucao.pack(pady=10)

        # Lista de seleção (Checkbox para cada ninja)
        self.scroll_frame = ctk.CTkScrollableFrame(self.sidebar, width=180, height=300)
        self.scroll_frame.pack(padx=10, pady=10)
        
        self.checkboxes = []
        for nome in self.df['Nome'].tolist():
            cb = ctk.CTkCheckBox(self.scroll_frame, text=nome)
            cb.pack(anchor="w", padx=10, pady=5)
            self.checkboxes.append(cb)

        self.btn_gerar = ctk.CTkButton(self.sidebar, text="Gerar Gráfico", command=self.atualizar_grafico)
        self.btn_gerar.pack(pady=20)

        # Área do Gráfico
        self.plot_area = ctk.CTkFrame(self)
        self.plot_area.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        
        self.canvas = None

    def atualizar_grafico(self):
        # Limpar gráfico anterior
        if self.canvas:
            self.canvas.get_tk_widget().destroy()

        selecionados = [cb.cget("text") for cb in self.checkboxes if cb.get()]
        
        if not selecionados:
            return

        # Lógica do Matplotlib (igual ao anterior)
        categorias = ['Ninjutsu', 'Taijutsu', 'Genjutsu', 'Inteligencia', 'Forca', 'Velocidade']
        num_vars = len(categorias)
        angulos = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
        angulos += angulos[:1]

        fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True), facecolor='#2b2b2b')
        ax.set_facecolor('#2b2b2b')

        for nome in selecionados:
            dados = self.df[self.df['Nome'] == nome]
            valores = dados[categorias].values.flatten().tolist()
            valores += valores[:1]
            cor = dados['Cor'].values[0]
            
            ax.plot(angulos, valores, color=cor, linewidth=2, label=nome)
            ax.fill(angulos, valores, color=cor, alpha=0.2)

        # Estilo do gráfico para combinar com o Dark Mode
        ax.set_ylim(0, 5)
        ax.tick_params(colors='white')
        ax.xaxis.label.set_color('white')
        plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

        # Integrar Matplotlib no CustomTkinter
        self.canvas = FigureCanvasTkAgg(fig, master=self.plot_area)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

if __name__ == "__main__":
    app = AppHyuga()
    app.mainloop()