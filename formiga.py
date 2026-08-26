

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
                
    def calcular_densidade_local(self, mapa):
        corpos = 0
        celulas_vistas = 0
        
        altura = len(mapa.matriz)
        largura = len(mapa.matriz[0])
        
        for dy in range( -self.raio, self.raio+1):
            for dx in range(-self.raio, self.raio+1):
                
                if(dx == 0 and dy ==0):
                    continue # Propria posicao da formiga
                
                celulas_vistas += 1
                
                if(mapa.matriz[dy][dx] == 'C'):
                    corpos += 1    

        if(celulas_vistas == 0):
            return 0
        
        return corpos/celulas_vistas