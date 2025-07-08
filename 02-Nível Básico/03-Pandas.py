#%%
# Manipulando dados em um Dataframe do Pandas
import pandas as pd
print("Versão do Pandas atual:",pd.__version__)

df = pd.DataFrame({'Numeros': [1, 2, 3]})
df

# %%
# Cria um dicionário
dados = {"Estado": ["Santa Catarina", "Rio de Janeiro", "Tocantins", "Bahia", "Minas Gerais"],
         "Ano": [2004, 2005, 2006, 2007, 2008],
         "Taxa Desemprego": [1.5, 1.7, 1.6, 2.4, 2.7]}

df = pd.DataFrame(dados)
df.head()


# %%
# Reorganizando as colunas
from pandas import DataFrame

DataFrame(dados, columns = ["Estado", "Taxa Desemprego", "Ano"])

# %%
# Criando outro dataframe com os mesmo dados anteriores, mas adicionando uma coluna
df2 = DataFrame(dados, 
                columns=["Estado", "Taxa Desemprego", "Taxa Crescimento", "Ano"],
                index = ["estado1", "estado2", "estado3", "estado4", "estado5",])

print("Colunas:", df2.columns)
print("Tipo das Colunas:\n",df2.dtypes)
df2

# %%
# Imprimindo apenas duas colunas
print(df2[["Taxa Desemprego", "Ano"]])

print("\n",df2.index)

# Filtrando pelo índice
df2.filter(items= ["estado3"], axis=0)

# %%
# Usando Numpy e Pandas Para Manipulação de Dados
print("Resumo estatístico do Dataframe")
df2.describe()

# %%
print("O Dataframe tem valores ausentes:\n", df2.isna())

# Usando o Numpy para alimentar uma das colunas do dataframe
import numpy as np
df2["Taxa Crescimento"] = np.arange(5.)
df2

# %%
# Slicing de DataFrames do Pandas
print("Fatiamento de dados do índice 2 ao 4, inclusivo.")
df2["estado2":"estado4"]

# %%
# Retornando dados onde a Taxa Desemprego é menor do que 2
df2[df2["Taxa Desemprego"] < 2]

# %%
# Preenchendo Valores Ausentes em DataFrames do Pandas
print("Importando um dataset.")
df_dsa = pd.read_csv("arquivos/dataset2.csv")

print("Retornando a soma da quantidade de dados ausentes.")
df_dsa.isna().sum()

# %%
# A moda em Estatística é uma medida de tendencia central que representa o valor mais frequente em um conjunto de dados.
# É útil quando queremos saber o valor mais comum ou popular em um conjunto de dados.
print("Extraindo a moda da coluna Quantidade.")
moda = df_dsa["Quantidade"].value_counts().index[0]
print("A moda é", moda)

# E por fim preenchemos os valores NA com a moda
df_dsa["Quantidade"].fillna(value=moda, inplace=True)
df_dsa.isna().sum()

# %%
# Query de Dados no DataFrame do Pandas
print("Checando os valores mínimo e máximo da coluna Valor_Venda")
df_dsa.Valor_Venda.describe()


# %%
# Gerando um novo Dataframe apenas com o intervalo de vendas entre 229 e 10000
df3 = df_dsa.query("229 < Valor_Venda < 1000")
df3.head()

# %%
# Verificando a Ocorrência de Diversos Valores em Uma Coluna
print("Linhas e Colunas do DataFrame:", df_dsa.shape)

# Aplicando filtro na coluna Quantidade
df_dsa[df_dsa["Quantidade"].isin([5, 7, 9, 11])]

# %%
# Operadores Lógicos Para Manipulação de Dados - &, |
# Filtrando as vendas que ocorreram para o segmento de Home Office e na região South
df_dsa[(df_dsa.Segmento == "Home Office") & (df_dsa.Regiao == "South")].head()


# %%
# Agrupamento de Dados em DataFrames com Group By
df_dsa[["Segmento", "Regiao", "Valor_Venda"]].groupby(["Segmento", "Regiao"]).mean()

# %%
# Agregação Múltipla com Group By
df_dsa[["Segmento", "Regiao", "Valor_Venda"]].groupby(["Segmento", "Regiao"]).agg(["mean", "std", "count"])

# %%
# Filtrando DataFrame com Base em Strings - str.startwith, str.endtwith
df_dsa[df_dsa.Segmento.str.startswith("Con")].head()


# %%
# Split de Strings em DataFrame, dividindo o ID a cada '-'
df_dsa["ID_Pedido"].str.split("-")

# %%
print("Extraindo o ano do ID_Pedido")
df_dsa["ID_Pedido"].str.split("-").str[1].head()


# %%
# Fazemos o split da coluna e extrapimos o pitem na posição 2 (índice 1)
df_dsa["Ano"] = df_dsa["ID_Pedido"].str.split("-").str[1]
df_dsa

# %%
# Strip de Strings em DataFrame. O Strip remove caracteres da string - lstrip, rstrip, strip().
df_dsa["Data_Pedido"].head(3)

print("Deixando o ano com apenas 2 dígitos sem alterar o tipo da variável")
df_dsa["Data_Pedido"].str.lstrip("20")

# Como não usamos o inplace=True a mudança é somente na memória e não afeta o dataframe.

# %%
# Replace de Strings em DataFrames - substitui caracteres dentro de uma string
print("Substituíndo os caracteres CG por AX na coluna 'ID_Cliente'.")
df_dsa["ID_Cliente"] = df_dsa["ID_Cliente"].str.replace("CG", "AX")
df_dsa.head()


# %%
# Combinação de Strings em DataFrames
print("Concatenando strings.")
df_dsa["Pedido_Segmento"] = df_dsa["ID_Pedido"].str.cat(df_dsa["Segmento"], sep="-")
df_dsa.head()


# %%
# Construção de Gráficos a Partir de DataFrames
# Instalar a versão exata do Scikit-learn
#!pip install -q scikit-learn==1.2.1
#import sklearn
#sklearn.__version__
#from sklearn.datasets import load_iris
#data = load_iris()

#import pandas as pd
#df = pd.DataFrame(data["data"], columns = data["feature_names"])
#df["species"] = data["target"]
#df.head()

#print("Para criar um gráfico de linhas com todas as variáveis do dataframe, basta fazer isso:")
#df.plot()

#print("Scatter plot com duas variáveis")
#df.plot.scatter(x="sepal length (cm)", y="sepal width (cm)")


#columns = ["sepal length (cm)", "petal length (cm)", "petal width (cm)", "sepal width (cm)"]
#df[columns].plot.area()

# Calculando a média das colunas agrupando pela coluna species e criamos um gráfico de barras com o resultado.
#df.groupby("species").mean().plot.bar()

# Contagem de classes da coluna species e plotamos em um gráfico de pizza
#df.groupby("species").count().plot.pie(y="sepal length (cm)")

