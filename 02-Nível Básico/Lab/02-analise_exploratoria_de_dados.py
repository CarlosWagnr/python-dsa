#%%
# Importando pacotes
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns
import datetime as dt

# CARREGANDO OS DADOS
df_dsa = pd.read_csv(r"..\arquivos\dataset.csv")
print("Linhas e Colunas", df_dsa.shape)

#%%
# AMOSTRA DOS DADOS
df_dsa.head()

#%%
# 01- Qual Cidade com Maior Valor de Venda de Produtos da Categoria 'Office Supplies'?

# Filtramos o dataframe com os registros da categoria que desejamos
df_dsa_p1 = df_dsa[df_dsa["Categoria"] == "Office Supplies"]

# Em seguida agrupamos por cidade e calculamos o total de valor_venda
df_dsa_p1_total = df_dsa_p1.groupby("Cidade")["Valor_Venda"].sum()

# Então encontramos a cidade com maior valor de vendas
cid_maior_valor = df_dsa_p1_total.idxmax()
print("Cidade com maior valor de venda para Office Supplies:", cid_maior_valor)

# Para conferir o resultado
df_dsa_p1_total.sort_values(ascending=False)

# %%
# 02- Qual o Total de Vendas Por Data do Pedido?
# Demonstre o resultado através de um gráfico de barras.


# %%
# 03- Qual o Total de Vendas por Estado?
# Demonstre o resultado através de um gráfico de barras.



# %%
# 04- Quais São as 10 Cidades com Maior Total de Vendas?
# Demonstre o resultado através de um gráfico de barras.



# %%
# 05- Qual Segmento Teve o Maior Total de Vendas?
# Demonstre o resultado através de um gráfico de pizza.


# %%
# 06- Qual o Total de Vendas Por Segmento e Por Ano?


# %%
# 07- Os  gestores  da  empresa  estão  considerando conceder  diferentes  faixas  de  
# descontos  e gostariam de fazer uma simulação com base na regra abaixo:
# Se o Valor_Venda for maior que 1000 recebe 15% de desconto.
# Se o Valor_Venda for menor que 1000 recebe 10% de desconto.
# Quantas Vendas Receberiam 15% de Desconto?



# %%
# 08- Considere  Que  a  Empresa  Decida  Conceder  o  Desconto  de  15%  do  Item  Anterior.
# Qual Seria a Média do Valor de Venda Antes e Depois do Desconto?



# %%
# 09- Qual o Média de Vendas Por Segmento, Por Ano e Por Mês?
# Demonstre o resultado através de gráfico de linha.



# %%
# 10- Qual o Total de Vendas Por Categoria e SubCategoria, Considerando Somente as Top 12 SubCategorias?
# Demonstre tudo através de um único gráfico
