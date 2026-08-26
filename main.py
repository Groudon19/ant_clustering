import random as r
import subprocess

from time import sleep

from mapa import Mapa
from formiga import Formiga
from corpo import Corpo

def print_mapa(mapa, corpos, formigas):
    
    for corpo in corpos:
        mapa.matriz[corpo.x][corpo.y] = 'C'
        
    for formiga in formigas:
        mapa.matriz[formiga.x][formiga.y] = 'F'
    
    for i in range(mapa.largura):
        for j in range(mapa.altura):
            print(mapa.matriz[i][j], end=' ')
        print(end='\n')

if __name__ == '__main__':
    
    ALTURA = 50
    LARGURA = 50
    
    NUM_FORMIGAS = 15
    NUM_CORPOS = 600
    
    ITERACOES = 1
    
    mapa = Mapa(ALTURA, LARGURA)
    formigas = []
    corpos = []
    
    for i in range(NUM_CORPOS):
        x = r.randint(0, LARGURA-1)
        y = r.randint(0, ALTURA-1)
        if mapa.matriz[x][y] == ' ':
            corpos.append(Corpo(x, y))
            mapa.matriz[x][y] = 'C'
        else:
            i -= 1
    
    for i in range(NUM_FORMIGAS):
        x = r.randint(0, LARGURA-1)
        y = r.randint(0, ALTURA-1)
        if mapa.matriz[x][y] == ' ':
            formigas.append(Formiga(x, y, 1))
            mapa.matriz[x][y] = 'F'
        else:
            #TODO: Analisar se formiga pode nascer em cima de corpo ou não
            i -= 1
    
    
    for i in range(ITERACOES):
        
        for formiga in formigas:
            mapa.matriz[formiga.x][formiga.y] = ' '
            direcao = r.choice(['cima', 'baixo', 'esquerda', 'direita'])
            formiga.mover(direcao, LARGURA, ALTURA)
            
        print_mapa(mapa, corpos, formigas)
        
        densidade = formigas[0].calcular_densidade_local(mapa)
        print(formigas[0].x, formigas[0].y)
        print(f'Densidade local da formiga 0: {densidade}')
        sleep(0.5)
        subprocess.call('clear', shell=True)
        
        pass
    
    