import random as r
import subprocess

from time import sleep

from mapa import Mapa
from formiga import Formiga
from corpo import Corpo

def print_mapa(mapa, corpos, formigas):
    
    # for corpo in corpos:
    #     mapa.matriz[corpo.y][corpo.x] = 'C'
        
    # for formiga in formigas:
    #     mapa.matriz[formiga.y][formiga.x] = 'F'
    
    for i in range(mapa.largura):
        for j in range(mapa.altura):
            print(mapa.matriz[i][j] if not mapa.matriz[i][j] == 'F' else ' ', end=' ')
        print(end='\n')


def carregar_corpos(caminho):
    corpos = []

    with open(caminho, 'r') as f:
        for linha in f:
            linha = linha.strip()

            if linha == "" or linha.startswith("#"):
                continue

            partes = linha.split()

            x = float(partes[0].replace(",", "."))
            y = float(partes[1].replace(",", "."))
            grupo = int(partes[2])

            corpos.append(Corpo(x, y, grupo))

    return corpos


if __name__ == '__main__':
    
    ALTURA = 50
    LARGURA = 50
    
    NUM_FORMIGAS = 15
    NUM_CORPOS = 600
    
    ITERACOES = 100000
    
    mapa = Mapa(ALTURA, LARGURA)
    formigas = []
    corpos = []
    
    for i in range(NUM_CORPOS):
        x = r.randint(0, LARGURA-1)
        y = r.randint(0, ALTURA-1)
        if mapa.matriz[y][x] == ' ':
            corpos.append(Corpo(x, y))
            mapa.matriz[y][x] = 'C'
        else:
            i -= 1
    
    for i in range(NUM_FORMIGAS):
        x = r.randint(0, LARGURA-1)
        y = r.randint(0, ALTURA-1)
        if mapa.matriz[y][x] == ' ':
            formigas.append(Formiga(x, y, 1))
            mapa.matriz[y][x] = 'F'
        else:
            #TODO: Analisar se formiga pode nascer em cima de corpo ou não
            i -= 1
    
    
    for i in range(ITERACOES):
        
        for formiga in formigas:
            
            
            x = formiga.x
            y = formiga.y

            if formiga.ocupado:
                if mapa.matriz[y][x] == ' ': # só pode largar em célula vazia
                    p_largar = formiga.probabilidade_largar(mapa)
                    if r.random() < p_largar:
                        #corpos.append(Corpo(x, y))
                        mapa.matriz[y][x] = 'C'
                        corpos.append(Corpo(x,y))
                        formiga.ocupado = False
                        
            else:
                if mapa.matriz[y][x] == 'C':
                    p_pegar = formiga.probabilidade_pegar(mapa)
                    if r.random() < p_pegar:
                        mapa.matriz[y][x] = ' '
                        corpos = [corpo for corpo in corpos
                                  if corpo.x != x or corpo.y != y]
                        formiga.ocupado = True
            
            direcao = r.choice(['cima', 'baixo', 'esquerda', 'direita'])
            formiga.mover(direcao, LARGURA, ALTURA)
            
        if i == 1 or i == 99999:
            print(f'Iteracao {i + 1}')
            print_mapa(mapa, corpos, formigas)
        
        # densidade = formigas[0].calcular_densidade_local(mapa)
        # print(formigas[0].y, formigas[0].x)
        # print(f'Densidade local da formiga 0: {densidade}')
        # sleep(0.5)
        #subprocess.call('clear', shell=True)
        
        pass
    
    