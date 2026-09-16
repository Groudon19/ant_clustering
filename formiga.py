

class Formiga:
    
    def __init__(self, x, y, raio):
        self.x = x
        self.y = y
        self.raio = raio
        self.corpo = None
        
    @property
    def ocupado(self):
        return self.corpo is not None
        
    def mover(self, direcao, largura, altura):
        if direcao == 'cima':
            self.y = (self.y - 1) % altura
        elif direcao == 'baixo':
            self.y = (self.y + 1) % altura
        elif direcao == 'esquerda':
            self.x = (self.x - 1) % largura
        elif direcao == 'direita':
            self.x = (self.x + 1) % largura
                
    def calcular_densidade_local(self, mapa):
        corpos = 0
        celulas_vistas = 0

        altura = mapa.altura
        largura = mapa.largura
        
        for dy in range(-self.raio, self.raio+1):
            for dx in range(-self.raio, self.raio+1):

                if(dx == 0 and dy ==0):
                    continue

                x = (self.x + dx) % largura
                y = (self.y + dy) % altura
                celulas_vistas += 1

                if mapa.get_corpo(x,y) is not None:
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