

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

        altura = mapa.altura
        largura = mapa.largura
        
        for dy in range( -self.raio, self.raio+1):
            for dx in range(-self.raio, self.raio+1):

                if(dx == 0 and dy ==0):
                    continue

                x = (self.x + dx) % largura
                y = (self.y + dy) % altura
                celulas_vistas += 1

                if mapa.matriz[y][x] == 'C':
                    corpos += 1

        if(celulas_vistas == 0):
            return 0

        return corpos/celulas_vistas
    
    def probabilidade_pegar(self, mapa):
        densidade = self.calcular_densidade_local(mapa)
        return  1 - densidade
    
    def probabilidade_largar(self, mapa):
        densidade = self.calcular_densidade_local(mapa)
        return densidade