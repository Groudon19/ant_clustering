# utils.py
def carregar_e_normalizar_base(caminho_arquivo):
    dados = []
    grupos = []

    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        for linha in f:
            linha_limpa = linha.strip()
            # Ignora linhas vazias ou comentários (#)
            if not linha_limpa or linha_limpa.startswith('#'):
                continue

            # Substitui vírgulas por pontos e separa por qualquer espaço/tab
            partes = linha_limpa.replace(',', '.').split()

            if len(partes) >= 3:
                # As primeiras colunas são os atributos numéricos (X, Y)
                atributos = [float(p) for p in partes[:-1]]
                # A última coluna é o grupo (1, 2, 3, 4)
                grupo = int(partes[-1])

                dados.append(atributos)
                grupos.append(grupo)

    num_atributos = len(dados[0])
    num_amostras = len(dados)

    # Normalização Linear Min-Max para cada atributo [0, 1]
    mins = [min(dados[i][j] for i in range(num_amostras)) for j in range(num_atributos)]
    maxs = [max(dados[i][j] for i in range(num_amostras)) for j in range(num_atributos)]

    dados_normalizados = []
    for i in range(num_amostras):
        linha_norm = []
        for j in range(num_atributos):
            amplitude = maxs[j] - mins[j]
            val_norm = (dados[i][j] - mins[j]) / amplitude if amplitude != 0 else 0.0
            linha_norm.append(val_norm)
        dados_normalizados.append(linha_norm)

    return dados_normalizados, grupos