import matplotlib.pyplot as plt
import numpy as np

def formatar_equacao(a, b, c):
    def formatar_coef(coef, var, is_quadratic=False):
        if coef == 0:
            return ""
        if coef == 1 and var:
            return f"+{var}" if not is_quadratic else var
        if coef == -1 and var:
            return f"-{var}"
        return f"{coef:+g}{var}"

    termo_a = formatar_coef(a, "x²", is_quadratic=True)
    termo_b = formatar_coef(b, "x")
    termo_c = formatar_coef(c, "")
    equacao = termo_a + termo_b + termo_c
    if equacao.startswith("+"):
        equacao = equacao[1:]
    return f"f(x) = {equacao}"

def plotar_grafico(a, b, c, raizes):
    x = np.linspace(-10, 10, 400)
    y = a * x**2 + b * x + c

    titulo = f"Gráfico de {formatar_equacao(a, b, c)}"

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label="f(x)", color="blue")

    plt.axhline(0, color='black', linewidth=1.2)
    plt.axvline(0, color='black', linewidth=1.2)

    texto_raizes = ""

    if raizes is not None:
        try:
            if len(raizes) == 1:
                texto_raizes = f"Raiz: x = {float(raizes[0]):.3g}"
                plt.plot(float(raizes[0]), 0, 'ro', label="Raiz")
            elif len(raizes) == 2:
                r1, r2 = raizes
                if isinstance(r1, complex) or isinstance(r2, complex):
                    def formatar_complexo(c):
                        real = f"{c.real:.3g}" if c.real != 0 else ""
                        imag = f"{abs(c.imag):.3g}i"
                        sinal = "+" if c.imag >= 0 and real else "-"
                        return f"{real}{sinal}{imag}" if real else f"{'-' if c.imag < 0 else ''}{imag}"

                    texto_raizes = f"Raízes imaginárias:\n" + \
                                f"x₁ = {formatar_complexo(r1)}\n" + \
                                f"x₂ = {formatar_complexo(r2)}"

                elif r1 == r2:
                    texto_raizes = f"Raízes iguais:\nx = {float(r1):.3g}"
                    plt.plot(float(r1), 0, 'ro', label="Raiz")
                else:
                    texto_raizes = f"Raízes reais:\n" + \
                                   f"x₁ = {float(r1):.3g}\n" + \
                                   f"x₂ = {float(r2):.3g}"
                    plt.plot(float(r1), 0, 'ro')
                    plt.plot(float(r2), 0, 'ro')
        except Exception as e:
            texto_raizes = f"Erro ao processar raízes: {e}"

    plt.title(titulo, fontsize=14)
    if texto_raizes:
        plt.text(0.05, 0.9, texto_raizes, fontsize=11, transform=plt.gca().transAxes,
                 verticalalignment='top')

    plt.grid(True)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.tight_layout()
    plt.show()
