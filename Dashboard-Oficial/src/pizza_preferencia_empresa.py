import pandas as pd
import plotly.express as px
import tabela_utils


def tirazero(tabela: pd.DataFrame):  # TODO remover ja que é inutil
    tabela = tabela.to_dict()
    apagar=[]
    for cabecalho in tabela:
        linhas = tabela[cabecalho]
        for index in linhas:
            if linhas[index] == 0:
                apagar.append(index)
    for linha in apagar:
        for coluna in tabela:
            tabela[coluna].pop(linha)
    return pd.DataFrame(tabela)


df=pd.read_csv('Dashboard-Oficial\data\ANAC20XX-13-14-15.csv',sep=';', encoding='latin')
df=tabela_utils.filtrar(df,['ANO', 'EMPRESA (NOME)','PASSAGEIROS PAGOS'])
df=tabela_utils.retirar_nulos(df)
df = tabela_utils.soma_por_categoria(df, 'EMPRESA (NOME)', 'PASSAGEIROS PAGOS')
df = tirazero(df) # TODO remover ja que é inutil

df1 = tabela_utils.outros(df, 'PASSAGEIROS PAGOS', 1500000)
df2 = tabela_utils.outros2(df, 'PASSAGEIROS PAGOS', 1500000) # TODO pq isso esta sendo feito se df2 nao é usada em lugar nenhum
print(df)

setores=px.pie(df1, names='EMPRESA (NOME)',values='PASSAGEIROS PAGOS', color_discrete_sequence=px.colors.qualitative.Prism, template='plotly_dark')
setores.show()