

class Mapa:
    
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura
        self.matriz = [[' ' for _ in range(largura)] for _ in range(altura)]
        self.corpos = {}
        
    def adicionar_corpo(self, corpo):
        self.corpos[(corpo.x, corpo.y)] = corpo
        self.matriz[corpo.y][corpo.x] = 'C'
        
    def remover_corpo(self, x, y):
        corpo = self.corpos.pop((x,y), None)
        self.matriz[y][x] = ' '
        return corpo
    
    def get_corpo(self, x, y):
        return self.corpos.get((x,y), None)
        
    def print(self):
        for i in range(self.altura):
            for j in range(self.largura):
                print(self.matriz[j][i], end=' ')
            print(end='\n')
        
                
    
                