

class Formiga:
    
    def __init__(self, x, y, raio, ocupado=False):
        self.x = x
        self.y = y
        self.raio = raio
        self.ocupado = ocupado
        
    def mover(self, direcao, largura, altura):
        if direcao == 'cima':
            self.y = self.y -1
            if self.y < 0:
                self.y = altura - 1
        elif direcao == 'baixo':
            self.y = self.y + 1
            if self.y >= altura:
                self.y = 0
        elif direcao == 'esquerda':
            self.x = self.x - 1
            if self.x < 0:
                self.x = largura - 1
        elif direcao == 'direita':
            self.x = self.x + 1
            if self.x >= largura:
                self.x = 0
        