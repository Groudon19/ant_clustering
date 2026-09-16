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


            