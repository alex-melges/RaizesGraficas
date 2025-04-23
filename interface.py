import tkinter as tk
from tkinter import messagebox
from calc_raizes import calcular_raizes
from graficos import plotar_grafico

def calcular():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a == 0 and b == 0:
            messagebox.showerror("Erro", "Insira pelo menos um valor diferente de zero para a ou b.")
            return

        tipo, raizes = calcular_raizes(a, b, c)
        plotar_grafico(a, b, c, raizes)

    except ValueError:
        messagebox.showerror("Erro", "Insira números válidos para os coeficientes.")

# Criando a janela principal
janela = tk.Tk()
janela.title("Raízes e Gráficos")

# Título
titulo = tk.Label(
    janela,
    text="Calculadora de Raízes e Gráficos\npara Polinômios de grau 1 e 2",
    font=("Arial", 14, "bold")
)
titulo.grid(row=0, column=0, columnspan=2, pady=10)

instrucao = tk.Label(
    janela,
    text="Digitar os coeficientes do polinômio ax² + bx + c",
    font=("Arial", 10)
)
instrucao.grid(row=1, column=0, columnspan=2, pady=(0, 10))

# Entrada dos coeficientes
tk.Label(janela, text="Coeficiente a:").grid(row=2, column=0, sticky="e")
entry_a = tk.Entry(janela)
entry_a.grid(row=2, column=1)

tk.Label(janela, text="Coeficiente b:").grid(row=3, column=0, sticky="e")
entry_b = tk.Entry(janela)
entry_b.grid(row=3, column=1)

tk.Label(janela, text="Coeficiente c:").grid(row=4, column=0, sticky="e")
entry_c = tk.Entry(janela)
entry_c.grid(row=4, column=1)

# Botão de calcular
botao = tk.Button(janela, text="Calcular Raízes e Exibir Gráfico", command=calcular)
botao.grid(row=5, column=0, columnspan=2, pady=10)

# Iniciar o loop da interface
janela.mainloop()
