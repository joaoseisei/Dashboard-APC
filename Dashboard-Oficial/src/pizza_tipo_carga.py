# ----------------------------------------- Importando bibliotecas -----------------------------------------
import pandas as pd
import plotly.express as px
import tabela_utils


# ---------------------------------------------- Lendo dataset ----------------------------------------------
print('Lendo dataset...') # Feedback
dados = pd.read_csv('Dashboard-Oficial\data\ANAC20XX-13-14-15.csv', sep = ';', encoding = 'latin') # Encoding resolve problema da acentuação


# --------------------------------------- Manipulando dados necessarios---------------------------------------
print('Filtrando dados colunas necessarias do dataset...') # Feedback
dados = tabela_utils.filtrar_colunas(dados, ['ANO', 'CARGA PAGA (KG)', 'CARGA GRÁTIS (KG)', 'CORREIO (KG)', 'BAGAGEM (KG)'])

print('Removendo valores invalidos...') # Feedback
dados = tabela_utils.retirar_nulos(dados)

print('Separando anos...') # Feedback
peso_2013 = tabela_utils.filtrar_linhas(dados, 'ANO', ['2013.0'])
peso_2014 = tabela_utils.filtrar_linhas(dados, 'ANO', ['2014.0'])
peso_2015 = tabela_utils.filtrar_linhas(dados, 'ANO', ['2015.0'])
# TODO Ver por que o retirar nulos esta transformando os numeros de ano em float

print('Filtrando fora coluna ano...') # Feedback
peso_2013 = tabela_utils.filtrar_colunas(peso_2013, ['CARGA PAGA (KG)', 'CARGA GRÁTIS (KG)', 'CORREIO (KG)', 'BAGAGEM (KG)'])
peso_2014 = tabela_utils.filtrar_colunas(peso_2014, ['CARGA PAGA (KG)', 'CARGA GRÁTIS (KG)', 'CORREIO (KG)', 'BAGAGEM (KG)'])
peso_2015 = tabela_utils.filtrar_colunas(peso_2015, ['CARGA PAGA (KG)', 'CARGA GRÁTIS (KG)', 'CORREIO (KG)', 'BAGAGEM (KG)'])

print('Somando tudo...') # Feedback
peso_2013_somado = tabela_utils.soma_generica_colunas(peso_2013)
peso_2014_somado = tabela_utils.soma_generica_colunas(peso_2014)
peso_2015_somado = tabela_utils.soma_generica_colunas(peso_2015)
# TODO transformar todas as funcoes a cima em uma unica que chama as outras


# -------------------------------- Futuro dropdown do Dashboard (Substituir) --------------------------------
print('De que ano gostaria de ver o grafico pizza? Digite 2013, 2014 ou 2015')
while True:
    ano_desejado = input()
    if ano_desejado == '2013':
        tabela_entrada_pizza = peso_2013_somado
        break
    elif ano_desejado == '2014':
        tabela_entrada_pizza = peso_2014_somado
        break
    elif ano_desejado == '2015':
        tabela_entrada_pizza = peso_2015_somado
        break
    else:
        print('Valor incorreto. Por favor digite 2013, 2014 ou 2015')


# ----------------------------------- TODO: Cai na fake news do caio -----------------------------------
tabela_entrada_pizza = tabela_entrada_pizza.transpose()
# O .transpose provavelmente nao é permitido. Mas sehundo o Mago de APC nao é necesssario fazer a mudanca de eixos. Eu nao consegui plotar a figura sem mudar os eixos entao esse cara vai ficar aqui ate eu a) fazer uma funcao pra substituir ou b) fazer funcionar sem a transposicao de eixos


# ----------------------------------------- Criando gráfico de pizza -----------------------------------------
print('Produzindo gráfico...') # Feedback
pizza = px.pie(tabela_entrada_pizza,
                values = 1,
                names = 0,
                hole = .4,
                template = 'plotly_dark',
                color_discrete_sequence = px.colors.qualitative.Prism,
                title = 'Percentual de peso transportado pelos aviões no Brasil em ' + ano_desejado
                )

pizza.update_traces(
        text =  ['CARGA PAGA', 'CARGA GRÁTIS', 'CORREIO', 'BAGAGEM'],
        textinfo = "text + percent", 
        textposition = 'outside',
        hovertemplate = '%{value} Kg',
        marker = dict(line = dict(color = 'rgb(17, 17, 17)', width = 3))
        )


# ---------------------------------------- Mostrando gráfico de pizza ----------------------------------------
print('Mostrando gráfico...') # Feedback
pizza.show()