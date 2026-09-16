

class Corpo:
    
    def __init__(self, x, y, atributos, grupo):
        self.x = x
        self.y = y
        # cada corpo tem um vetor com n atributos (float)
        self.atributos = atributos
        self.grupo = grupo