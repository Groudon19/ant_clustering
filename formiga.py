

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
                
    def calcular_densidade_local(self, mapa, corpo_alvo, alpha=0.5):
        soma_similaridade = 0
        celulas_vistas = 0

        altura = mapa.altura
        largura = mapa.largura
        
        for dy in range(-self.raio, self.raio+1):
            for dx in range(-self.raio, self.raio+1):

                if(dx == 0 and dy ==0):
                    continue

                x = (self.x + dx) % largura
                y = (self.y + dy) % altura
                # Esse celulas vistas é sempre as 8 em um raio de 1, ou deveria ser só os vizinhos que tem corpo?
                celulas_vistas += 1

                corpo_vizinho = mapa.get_corpo(x,y)
                if corpo_vizinho is not None:
                    distancia = corpo_alvo.calcular_distancia(corpo_vizinho)
                    soma_similaridade += 1 - distancia / alpha

        if(celulas_vistas == 0):
            return 0
        
        # print(f'Soma similaridade: {soma_similaridade}')
        
        f_xi = (1/celulas_vistas ** 2) * max(0, soma_similaridade)
        
        # print(f'Densidade local da formiga em ({self.x}, {self.y}) com corpo {corpo_alvo.grupo}: {f_xi}')
        
        return f_xi
    
    def probabilidade_pegar(self, mapa, corpo_alvo, k1=0.1, alpha=0.5):
        f_xi = self.calcular_densidade_local(mapa, corpo_alvo, alpha)
        return  (k1 / (k1 + f_xi)) ** 2
    
    def probabilidade_largar(self, mapa, k2=0.15, alpha=0.5):
        f_xi = self.calcular_densidade_local(mapa, self.corpo, alpha=0.5)
        return (f_xi / (k2 + f_xi)) ** 2