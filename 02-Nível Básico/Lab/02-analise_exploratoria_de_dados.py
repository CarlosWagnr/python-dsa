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



# %%
# 09- Qual o Média de Vendas Por Segmento, Por Ano e Por Mês?
# Demonstre o resultado através de gráfico de linha.



# %%
# 10- Qual o Total de Vendas Por Categoria e SubCategoria, Considerando Somente as Top 12 SubCategorias?
# Demonstre tudo através de um único gráfico
