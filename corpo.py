# corpo.py
import math

class Corpo:
    def __init__(self, x, y, atributos, grupo=None):
        self.x = x
        self.y = y
        self.atributos = atributos  # Lista de floats normalizados: [a1, a2, ...]
        self.grupo = grupo          # Identificador do grupo (1, 2, 3, 4)

    def calcular_distancia(self, outro_corpo):
        """Calcula a distância euclidiana entre dois corpos no espaço de atributos."""
        soma_quadrados = sum((a - b) ** 2 for a, b in zip(self.atributos, outro_corpo.atributos))
        return math.sqrt(soma_quadrados)