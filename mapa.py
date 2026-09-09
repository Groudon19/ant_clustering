# mapa.py
class Mapa:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura
        self.matriz = [[' ' for _ in range(largura)] for _ in range(altura)]
        self.grade_corpos = {}  # Mapeia (x, y) -> objeto Corpo

    def adicionar_corpo(self, corpo):
        self.grade_corpos[(corpo.x, corpo.y)] = corpo
        self.matriz[corpo.y][corpo.x] = 'C'  # ou str(corpo.grupo) para debug

    def remover_corpo(self, x, y):
        corpo = self.grade_corpos.pop((x, y), None)
        self.matriz[y][x] = ' '
        return corpo

    def obter_corpo_em(self, x, y):
        return self.grade_corpos.get((x, y), None)