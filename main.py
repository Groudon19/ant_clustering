from mapa import Mapa

def print_mapa(mapa):
    for i in range(mapa.largura):
        for j in range(mapa.altura):
            print(mapa.matriz[i][j], end=' ')
        print(end='\n')

if __name__ == '__main__':
    
    ALTURA = 50
    LARGURA = 50
    ITERACOES = 100000
    
    mapa = Mapa(ALTURA, LARGURA)
    formigas = []
    corpos = []
    
    
    
    for i in range(ITERACOES):
        print_mapa(mapa)
        pass
    
    