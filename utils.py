def carregar_atributos_e_grupos(caminho_arquivo):
    atributos = []
    grupos = []
    with open(caminho_arquivo, 'r') as arquivo:
        for linha in arquivo:
            linha_limpa = linha.strip()
            
            if not linha_limpa or linha_limpa.startswith('#'):
                continue
            
            partes = linha_limpa.replace(',', '.').split()
            if len(partes) < 2:
                continue
            
            atributos.append([float(atributo) for atributo in partes[:-1]])
            grupos.append(partes[-1])
            
    return atributos, grupos

def normaliza_atributos(lista_de_atributos):
    if not lista_de_atributos:
        return []
    
    min_valores = [min(atributos) for atributos in zip(*lista_de_atributos)]
    max_valores = [max(atributos) for atributos in zip(*lista_de_atributos)]
    
    lista_normalizada = []
    for atributos in lista_de_atributos:
        atributos_normalizados = [
            (atributo - min_val) / (max_val - min_val) if max_val != min_val else 0.0
            for atributo, min_val, max_val in zip(atributos, min_valores, max_valores)
        ]
        lista_normalizada.append(atributos_normalizados)
        # print(f'Atributos originais: {atributos}, Atributos normalizados: {atributos_normalizados}')
        
    return lista_normalizada