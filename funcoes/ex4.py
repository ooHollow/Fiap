#usei classe fds!
import math
class Equacao:
    def __init__(self, a, b, c):
        if a == 0:
            raise ValueError
        self.a = a
        self.b = b
        self.c = c
    def delta(self):
        return (self.b**2) - 4*self.a*self.c
    def raizes(self):
        if self.delta() < 0:
            raise ValueError
        x1 = (-self.b + math.sqrt(self.delta())) / (2*self.a)
        x2 = (-self.b - math.sqrt(self.delta())) / (2*self.a)
        if self.delta() > 0:
            return x1, x2
        else:
            return x1
    def vertices(self):
        x = -self.b/(2*self.a)
        y = -self.delta()/(4*self.a)
        return x, y
    def __str__(self):
        return f"{self.a}x² + ({self.b})x + ({self.c}) = 0"

try:
    conta = Equacao(1, -5, 6)
    print(f"Equação: {conta}")
    print(f"Delta: {conta.delta()}")
    print(f"Raízes: {conta.raizes()}")
    print(f"Vértice: {conta.vertices()}")
except ValueError as e:
    print(e)