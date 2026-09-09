# formiga.py
class Formiga:
    def __init__(self, x, y, raio=2):
        self.x = x
        self.y = y
        self.raio = raio
        self.corpo_carregado = None  # None quando livre, armazena objeto Corpo quando ocupado

    @property
    def ocupado(self):
        return self.corpo_carregado is not None

    def mover(self, direcao, largura, altura):
        if direcao == 'cima':
            self.y = (self.y - 1) % altura
        elif direcao == 'baixo':
            self.y = (self.y + 1) % altura
        elif direcao == 'esquerda':
            self.x = (self.x - 1) % largura
        elif direcao == 'direita':
            self.x = (self.x + 1) % largura

    def calcular_f(self, mapa, corpo_alvo, alpha=0.5):
        """
        Calcula f(x_i): densidade/similaridade local do corpo_alvo.
        alpha: parâmetro de escala de dissemelhança.
        """
        soma_similaridade = 0.0
        celulas_vistas = 0

        for dy in range(-self.raio, self.raio + 1):
            for dx in range(-self.raio, self.raio + 1):
                if dx == 0 and dy == 0:
                    continue

                x = (self.x + dx) % mapa.largura
                y = (self.y + dy) % mapa.altura
                celulas_vistas += 1

                # Verifica se há um Corpo na posição
                corpo_vizinho = mapa.obter_corpo_em(x, y)
                if corpo_vizinho is not None:
                    distancia = corpo_alvo.calcular_distancia(corpo_vizinho)
                    # Termo de similaridade (quanto menor a distância, maior a contribuição)
                    soma_similaridade += max(0.0, 1.0 - (distancia / alpha))

        if celulas_vistas == 0:
            return 0.0

        f_xi = soma_similaridade / celulas_vistas
        return max(0.0, min(1.0, f_xi))  # Garante f(x_i) em [0, 1]

    def probabilidade_pegar(self, mapa, corpo_alvo, k1=0.1, alpha=0.5):
        f_xi = self.calcular_f(mapa, corpo_alvo, alpha)
        return (k1 / (k1 + f_xi)) ** 2

    def probabilidade_largar(self, mapa, corpo_alvo, k2=0.15, alpha=0.5):
        f_xi = self.calcular_f(mapa, corpo_alvo, alpha)
        return (f_xi / (k2 + f_xi)) ** 2