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
