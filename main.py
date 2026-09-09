# main.py
import random as r
from mapa import Mapa
from formiga import Formiga
from corpo import Corpo
from utils import carregar_e_normalizar_base

def print_mapa_grupos(mapa, formigas):
    # Cria uma cópia visual temporária
    matriz_visual = [linha[:] for linha in mapa.matriz]

    # Desenha as formigas
    for f in formigas:
        matriz_visual[f.y][f.x] = 'F'

    # Imprime no terminal
    for i in range(mapa.altura):
        linha_str = ""
        for j in range(mapa.largura):
            corpo = mapa.obter_corpo_em(j, i)
            if matriz_visual[i][j] == 'F':
                linha_str += ' '
            elif corpo is not None:
                linha_str += f'{corpo.grupo} '
            else:
                linha_str += ' '
        print(linha_str)



if __name__ == '__main__':
    ALTURA, LARGURA = 50, 50
    NUM_FORMIGAS = 15
    ITERACOES = 100000
    K1, K2 = 0.3, 0.05
    ALPHA = 2.0

    # 1. Carrega e normaliza os dados da base sintética
    dados_norm, grupos = carregar_e_normalizar_base('base4.txt')
    
    mapa = Mapa(ALTURA, LARGURA)
    
    # 2. Inicializa Corpos no mapa
    for attrs, grp in zip(dados_norm, grupos):
        while True:
            x, y = r.randint(0, LARGURA - 1), r.randint(0, ALTURA - 1)
            if mapa.obter_corpo_em(x, y) is None:
                corpo = Corpo(x, y, attrs, grp)
                mapa.adicionar_corpo(corpo)
                break

    # 3. Inicializa Formigas
    formigas = [Formiga(r.randint(0, LARGURA - 1), r.randint(0, ALTURA - 1), raio=2) 
                for _ in range(NUM_FORMIGAS)]

    # 4. Loop de Simulação
    for iteracao in range(ITERACOES):
        for formiga in formigas:
            x, y = formiga.x, formiga.y

            if formiga.ocupado:
                # Se a posição atual está vazia, avalia largar o corpo
                if mapa.obter_corpo_em(x, y) is None:
                    p_largar = formiga.probabilidade_largar(mapa, formiga.corpo_carregado, k2=K2, alpha=ALPHA)
                    if r.random() < p_largar:
                        corpo_para_soltar = formiga.corpo_carregado
                        corpo_para_soltar.x, corpo_para_soltar.y = x, y
                        mapa.adicionar_corpo(corpo_para_soltar)
                        formiga.corpo_carregado = None
            else:
                # Se há um corpo na posição atual, avalia pegar
                corpo_no_local = mapa.obter_corpo_em(x, y)
                if corpo_no_local is not None:
                    p_pegar = formiga.probabilidade_pegar(mapa, corpo_no_local, k1=K1, alpha=ALPHA)
                    if r.random() < p_pegar:
                        formiga.corpo_carregado = mapa.remover_corpo(x, y)

            # Move a formiga para a próxima posição
            direcao = r.choice(['cima', 'baixo', 'esquerda', 'direita'])
            formiga.mover(direcao, LARGURA, ALTURA)
            
            
    #Exibir o mapa a cada 50000 iterações
    if(iteracao+1) % 50000 == 0:
        print(f"Iteração {iteracao+1}:")
        print_mapa_grupos(mapa, formigas)
        