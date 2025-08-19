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
df_dsa_p2 = df_dsa.groupby("Data_Pedido")["Valor_Venda"].sum()
df_dsa_p2.head()

# plot
plt.figure(figsize= (20, 6))
df_dsa_p2.plot(x = "Data_Pedido", y = "Valor_Venda", color = "green")
plt.title("Total de Vendas Por Data do Pedido")
plt.show()

# %%
# 03- Qual o Total de Vendas por Estado?
# Demonstre o resultado através de um gráfico de barras.
df_dsa_p3 = df_dsa.groupby("Estado")["Valor_Venda"].sum().reset_index()
df_dsa_p3.head()

# plot
#plt.figure(figsize= (16, 6))
#sns.barplot(data = df_dsa_p3, y = "Valor_Venda", x = "Estado").set(title="Vendas Por Estado")
#plt.xticks(rotation = 80)
#plt.show()

# %%
# 04- Quais São as 10 Cidades com Maior Total de Vendas?
# Demonstre o resultado através de um gráfico de barras.
df_dsa_p4 = df_dsa.groupby("Cidade")["Valor_Venda"].sum().reset_index().sort_values(by="Valor_Venda", ascending=False).head(10)
df_dsa_p4.head(10)

# plot
#plt.figure(figsize= (16, 6))
#sns.set_palette("coolwarm")
#sns.barplot(data = df_dsa_p4, y = "Valor_Venda", x = "Cidade").set(title="As 10 cidades com maior Total de Vendas")
#plt.show()

# %%
# 05- Qual Segmento Teve o Maior Total de Vendas?
# Demonstre o resultado através de um gráfico de pizza.
df_dsa_p5 = df_dsa.groupby("Segmento")["Valor_Venda"].sum().reset_index().sort_values(by="Valor_Venda", ascending=False)
df_dsa_p5.head()

# Função para converter os dados em valor absoluto
def autopct_format(values):
    def my_format(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return " $ {v:d}".format(v=val)
    return my_format

# plot
plt.figure(figsize=(16, 6))

# Gráfico de pizza
plt.pie(df_dsa_p5["Valor_Venda"], labels=df_dsa_p5["Segmento"],
        autopct = autopct_format(df_dsa_p5["Valor_Venda"]),
        startangle=90)

# Limpa o círculo central
centre_circle = plt.Circle((0, 0), 0.82, fc = "white")
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Labels e anotações
plt.annotate(text="Total de Vendas: "+ "$ "+ str(int(sum(df_dsa_p5["Valor_Venda"]))), xy=(-0.25, 0))
plt.title("Total de Vendas por Segmento")
plt.show()


# %%
# 06- Qual o Total de Vendas Por Segmento e Por Ano?
# Convertendo a coluna de data para o tipo datetime para obter o formato adequado
df_dsa["Data_Pedido"] = pd.to_datetime(df_dsa["Data_Pedido"], dayfirst=True)
#df_dsa.dtypes

# Extraindo o ano e criando uma nova variável
df_dsa["Ano"] = df_dsa["Data_Pedido"].dt.year
#df_dsa.head()

# Total de Vendas por Segmento e por Ano
df_dsa_p6 = df_dsa.groupby(["Ano", "Segmento"])["Valor_Venda"].sum()
df_dsa_p6


# %%
# 07- Os  gestores  da  empresa  estão  considerando conceder  diferentes  faixas  de descontos  e gostariam de fazer uma simulação com base na regra abaixo:
# Se o Valor_Venda for maior que 1000 recebe 15% de desconto.
# Se o Valor_Venda for menor que 1000 recebe 10% de desconto.
# Quantas Vendas Receberiam 15% de Desconto?

# Cria uma coluna de acordo com a regra definida
df_dsa["Desconto"] = np.where(df_dsa["Valor_Venda"] > 1000, 0.15, 0.10)
#df_dsa.head()

# Total por cada valor da variável
df_dsa["Desconto"].value_counts()
print("No total 457 Vendas Receberiam Desconto de 15%.")

# %%
# 08- Considere  Que  a  Empresa  Decida  Conceder  o  Desconto  de  15%  do  Item  Anterior.
# Qual Seria a Média do Valor de Venda Antes e Depois do Desconto?
# - Criamos uma coluna calculando o valor de venda menos o desconto
df_dsa["Valor_Venda_Desconto"] = df_dsa["Valor_Venda"] - (df_dsa["Valor_Venda"] * df_dsa["Desconto"])
df_dsa.head()

# Filtrando as vendas antes do desconto de 15%
df_dsa_p8_vendas_antes_desconto = df_dsa.loc[df_dsa["Desconto"] == 0.15, "Valor_Venda"]

# Filtrando as vendas depois do desconto de 15%
df_dsa_p8_vendas_depois_desconto = df_dsa.loc[df_dsa["Desconto"] == 0.15, "Valor_Venda_Desconto"]

# Calcula a média das vendas antes do desconto de 15%
media_vendas_antes_desconto = df_dsa_p8_vendas_antes_desconto.mean()

# Calcula a média das vendas depois do desconto de 15%
media_vendas_depois_desconto = df_dsa_p8_vendas_depois_desconto.mean()

print("Média das vendas antes do desconto de 15%:", round(media_vendas_antes_desconto, 2))
print("Média das vendas depois do desconto de 15%:", round(media_vendas_depois_desconto, 2))


# %%
# 09- Qual o Média de Vendas Por Segmento, Por Ano e Por Mês?
# Demonstre o resultado através de gráfico de linha.

# Extraimos o mês e gravamos em uma nova variável
df_dsa["Mes"] = df_dsa["Data_Pedido"].dt.month
df_dsa.head()

# Agrupamento por ano, mês e segmento e calculamos estatísticas de agregação
df_dsa_p9 = df_dsa.groupby(["Ano", "Mes", "Segmento"])["Valor_Venda"].agg([np.sum, np.mean, np.median])
df_dsa_p9

# Vamos extrair os níveis
anos = df_dsa_p9.index.get_level_values(0)
meses = df_dsa_p9.index.get_level_values(1)
segmento = df_dsa_p9.index.get_level_values(2)

# plot
#plt.figure(figsize = (12, 6))
#sns.set()
#figl = sns.relplot(kind = 'line',
#                   data = df_dsa_p9,
#                   y = 'mean',
#                   x = meses,
#                   hue = segmento,
#                   col = anos,
#                   col_wrap = 4
#                   )
#
#plt.show()



# %%
# 10- Qual o Total de Vendas Por Categoria e SubCategoria, Considerando Somente as Top 12 SubCategorias?
# Demonstre tudo através de um único gráfico
df_dsa.head()

# Agrupamos por categoria e subcategoria e calculamos a soma somente para variáveis numéricas
df_dsa_p10 = df_dsa.groupby(["Categoria", "SubCategoria"]).sum(numeric_only = True).sort_values("Valor_Venda", ascending=False).head(12)
#df_dsa_p10.head()

# Convertemos a coluna Valor_Venda em número inteiro e classificamos por categoria
df_dsa_p10 = df_dsa_p10[["Valor_Venda"]].astype(int).sort_values(by = "Categoria").reset_index()

# OBS: Classificar o item por categoria é importante para preencher o gráfico com as subcategorias para cada categoria de forma ordenada.
df_dsa_p10.head(10)


# %%
# Criamos outro dataframe somente com os totais por categoria
df_dsa_p10_cat = df_dsa_p10.groupby("Categoria").sum(numeric_only=True).reset_index()
df_dsa_p10_cat



# %%
# Lista de cores para categoria
cores_categorias = ["#5d00de",
                    "#0ee84f",
                    "#e80e27"]

# Lista de cores para Subcategorias
cores_subcategorias = ["#aa8cd4",
                       "#aa8cd5",
                       "#aa8cd6",
                       "#aa8cd7",
                       "#26c957",
                       "#26c958",
                       "#26c959",
                       "#26c960",
                       "#e65e65",
                       "#e65e66",
                       "#e65e67",
                       "#e65e68",]

# Plot

# Tamanho da figura
fig, ax = plt.subplots(figsize = (18, 12))

# Gráfico por categoria
p1 = ax.pie(df_dsa_p10_cat["Valor_Venda"],
            radius = 1,
            labels = df_dsa_p10_cat["Categoria"],
            wedgeprops=dict(edgecolor =  "white"),
            colors = cores_categorias)

# Gráfico das subcategorias
p2 = ax.pie(df_dsa_p10["Valor_Venda"],
            radius = 0.9,
            labels = df_dsa_p10["SubCategoria"],
            autopct=autopct_format(df_dsa_p10["Valor_Venda"]),
            colors=cores_subcategorias,
            labeldistance= 0.7,
            wedgeprops=dict(edgecolor =  "white"),
            pctdistance=0.53,
            rotatelabels=True)

# Limpa o centro do circulo
centre_circle = plt.Circle((0, 0), 0.6, fc = "white")

# Labels e anotações
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.annotate(text="Total de Vendas: " + "$ " + str(int(sum(df_dsa_p10["Valor_Venda"]))), xy = (-0.2, 0))
plt.title("Total de Vendas Por Categoria e Top 12 SubCategorias")
plt.show()



# %%
