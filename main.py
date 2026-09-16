import random as r
import subprocess

from time import sleep

from mapa import Mapa
from formiga import Formiga
from corpo import Corpo
from utils import carregar_atributos_e_grupos, normaliza_atributos

if __name__ == '__main__':
    
    ALTURA = 64
    LARGURA = 64
    
    NUM_FORMIGAS = 15
    # NUM_CORPOS = 600
    
    ITERACOES = 50000000
    
    K1, K2 = 0.5, 0.025
    ALPHA = 0.35
    
    mapa = Mapa(ALTURA, LARGURA)
    formigas = []
    
    atributos, grupos = carregar_atributos_e_grupos('base4.txt')
    atributos_normalizados = normaliza_atributos(atributos)
    
    for atributos_corpo, grupo_corpo in zip(atributos_normalizados, grupos):
        while True:
            x = r.randint(0, LARGURA-1)
            y = r.randint(0, ALTURA-1)
            if mapa.get_corpo(x,y) is None:
                mapa.adicionar_corpo(Corpo(x,y, atributos_corpo, grupo_corpo))
                break
    
    while len(formigas) < NUM_FORMIGAS:
        x = r.randint(0, LARGURA-1)
        y = r.randint(0, ALTURA-1)
        if mapa.get_corpo(x,y) is None:
            formigas.append(Formiga(x, y, 1))
            # mapa.matriz[y][x] = 'F'
    
    for i in range(ITERACOES):
        
        for formiga in formigas:
            
            
            x = formiga.x
            y = formiga.y
            flag_corpo = mapa.get_corpo(x,y) is not None

            if formiga.ocupado:
                if not flag_corpo: # só pode largar em célula vazia
                    p_largar = formiga.probabilidade_largar(mapa, K2, ALPHA)
                    # print(f'Probabilidade de largar: {p_largar}')
                    if r.random() < p_largar:
                        corpo_que_sera_solto = formiga.corpo
                        corpo_que_sera_solto.x, corpo_que_sera_solto.y = x, y
                        mapa.adicionar_corpo(corpo_que_sera_solto)
                        formiga.corpo = None
                        
            else:
                if flag_corpo:
                    p_pegar = formiga.probabilidade_pegar(mapa, mapa.get_corpo(x,y), K1, ALPHA)
                    # print(f'Probabilidade de pegar: {p_pegar}')
                    if r.random() < p_pegar:
                        formiga.corpo = mapa.remover_corpo(x, y)
            
            direcao = r.choice(['cima', 'baixo', 'esquerda', 'direita'])
            formiga.mover(direcao, LARGURA, ALTURA)
            
        if i % (ITERACOES // 10) == 0:
            print(f'Iteracao {i}')
            mapa.print()
        
        # densidade = formigas[0].calcular_densidade_local(mapa)
        # print(formigas[0].y, formigas[0].x)
        # print(f'Densidade local da formiga 0: {densidade}')
        
        # sleep(0.5)
        #subprocess.call('clear', shell=True)
        
        pass
    
    print(f'Iteracao {ITERACOES}')
    mapa.print()
    # mapa.print_corpos()
    
    