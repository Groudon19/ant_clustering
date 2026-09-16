from math import sqrt

class Corpo:
    
    def __init__(self, x, y, atributos, grupo):
        self.x = x
        self.y = y
        # cada corpo tem um vetor com n atributos (float)
        self.atributos = atributos
        self.grupo = grupo
        
    def calcular_distancia(self, outro_corpo):
        soma_quadrados = sum((a -b) ** 2 for a, b in zip(self.atributos, outro_corpo.atributos))
        # print(f'Distancia entre corpo {self.grupo} e corpo {outro_corpo.grupo}: {sqrt(soma_quadrados)}')
        return sqrt(soma_quadrados)