import math

def calcular_raizes(a: float, b: float, c: float):
    """Calcula as raízes da equação ax² + bx + c = 0"""
    if a == 0:
        # Equação de primeiro grau
        if b == 0:
            return None  # Nenhuma raiz (b = 0)
        x = -c / b
        return ("linear", [x])
    else:
        # Equação de segundo grau (Bhaskara)
        delta = b**2 - 4 * a * c
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            return ("quadratica", [x1, x2])
        elif delta == 0:
            x = -b / (2 * a)
            return ("quadratica", [x])
        else:
            parte_real = -b / (2 * a)
            parte_imaginaria = math.sqrt(-delta) / (2 * a)
            x1 = complex(parte_real, parte_imaginaria)
            x2 = complex(parte_real, -parte_imaginaria)
            return ("complexa", [x1, x2])
