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
# COLUNAS DO CONJUNTO DE DADOS
df_dsa.columns


# %%
# VERIFICANDO O TIPO DE CADA COLUNA
df_dsa.dtypes

# %%
# RESUMO ESTATÍSTICO DA COLUNA COM VALOR VENDA
df_dsa["Valor_Venda"].describe()


# %%
# VERIFIFCANDO SE HÁ REGISTROS DUPLICADOS
df_dsa[df_dsa.duplicated()]

# %%
# VERIFICANDO SE HÁ VALORES AUSENTES
df_dsa.isnull().sum()

