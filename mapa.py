

class Mapa:
    
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura
        self.matriz = [[' ' for _ in range(largura)] for _ in range(altura)]
        self.corpos = {}
        
    def adicionar_corpo(self, corpo):
        if (corpo.x, corpo.y) in self.corpos:
            # Se já existe um corpo na posição, ele é sobrescrito
            self.remover_corpo(corpo.x, corpo.y)
        self.corpos[(corpo.x, corpo.y)] = corpo
        self.matriz[corpo.y][corpo.x] = corpo.grupo
        
    def remover_corpo(self, x, y):
        corpo = self.corpos.pop((x,y), None)
        self.matriz[y][x] = ' '
        return corpo
    
    def get_corpo(self, x, y):
        return self.corpos.get((x,y), None)
        
    def print(self):
        for i in range(self.altura):
            for j in range(self.largura):
                print(self.matriz[i][j], end=' ')
            print()
        
    def print_corpos(self):
        for corpo in self.corpos.values():
            print(f'Corpo em ({corpo.x}, {corpo.y}) com atributos {corpo.atributos} e grupo {corpo.grupo}')
                
    
                