from cmath import isnan
import pandas as pd
import math
from collections  import defaultdict

def maximo(tabela: pd.DataFrame, cabecalho_max: str) -> float:
    """Calcula o valor máximo de uma coluna

    Args:
        tabela (pd.DataFrame): Tabela a ser operada
        cabecalho_max (str): coluna a ser operada

    Returns:
        float: Valor máximo dentro da coluna
    """
    linhas=tabela.values.tolist()
    cabecalhos=tabela.columns.to_list()
    maximo = 0
    for linha in linhas:
        atual=linha[cabecalhos.index(cabecalho_max)]
        if atual>maximo:
            maximo=atual
    return maximo


def soma_por_categoria(tabela: pd.DataFrame, cabecalho_categoria: str, cabecalho_a_somar: str) -> pd.DataFrame:
    """Soma os valores de uma coluna para cada valor diferente de outra coluna

    Args:
        tabela (pd.DataFrame): Tabela a ser operada
        cabecalho_categoria (str): Cabeçalho onde estão as categorias
        cabecalho_a_somar (str): Cabeçalho a ser calculada a soma

    Returns:
        pd.DataFrame: Dataframe com os dados calculados
    """
    # tabela = tabela.to_dict()

    # tabela_resultado={cabecalho_categoria:{},cabecalho_a_somar:{}}
    # coluna_a_somar = tabela[cabecalho_a_somar]
    # coluna_categoria = tabela[cabecalho_categoria]
    # soma={}
    
    # for index in coluna_categoria:
    #     valor_linha = coluna_categoria[index]
    #     if valor_linha in soma:
    #         soma[valor_linha]+=coluna_a_somar[index]
    #     else:
    #         soma[valor_linha]=coluna_a_somar[index]

    # linhas=len(soma)
    # i=1
    # for categoria in soma:
    #     tabela_resultado[cabecalho_categoria][i] = categoria
    #     tabela_resultado[cabecalho_a_somar][i] = soma[categoria]
    #     i+=1

    linhas = tabela.values.tolist()
    cabecalhos = tabela.columns.to_list()
    cat_index = cabecalhos.index(cabecalho_categoria)
    valor_index = cabecalhos.index(cabecalho_a_somar)

    resultado=defaultdict(float)
    for linha in linhas:
        resultado[linha[cat_index]]+=linha[valor_index]

    resultado_lista=[]
    for cat in resultado:
        resultado_lista.append([cat,resultado[cat]])

    return pd.DataFrame(resultado_lista, columns=[cabecalhos[cat_index],cabecalhos[valor_index]])
        
            


def filtrar(tabela: pd.DataFrame, filtros: list) -> pd.DataFrame: 
    """Função feita para filtrar colunas em Dataframes

    Args:
        tabela (pd.DataFrame): A tabela que será filtrada
        filtros (list): Lista de colunas que serão mantidas

    Returns:
        pd.DataFrame: Dataframe com as colunas filtradas
    """

    linhas = tabela.values.tolist()
    cabecalhos = tabela.columns.to_list()
    indexes=[]
    resultado=[]

    cabecalhos_filtrados=[]
    for cabecalho in cabecalhos:
        if cabecalho in filtros:
            indexes.append(cabecalhos.index(cabecalho))
            cabecalhos_filtrados.append(cabecalho)
    
    linha_filtrada=[]
    for linha in linhas:
        linha_filtrada=[]
        for index in indexes:
            linha_filtrada.append(linha[index])
        resultado.append(linha_filtrada)

    return pd.DataFrame(resultado, columns=cabecalhos_filtrados)


def retirar_nulos(tabela: pd.DataFrame) -> pd.DataFrame:
    """Retira todas as linhas que contenham qualquer valor NaN de uma tabela

    Args:
        tabela (pd.DataFrame): A tabela a ser operada

    Returns:
        pd.DataFrame: Uma tabela com os valores nulos retirados
    """

    linhas = tabela.values.tolist()
    cabecalhos = tabela.columns.to_list()
    linhas_resultado=[]
    invalido = False

    for linha in linhas:
        invalido = False
        for coluna in linha:
            if isinstance(coluna, float):
                if math.isnan(coluna):
                    invalido = True
                    break
        if not invalido:
            linhas_resultado.append(linha)
    
    return pd.DataFrame(linhas_resultado, columns=cabecalhos)
