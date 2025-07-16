#%%
# Seaborn - Statistical Data Visualization com Seabron
# pip install seaborn
import random
import numpy
import pandas as pd
import matplotlib as mat
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

# Criando Gráficos com Seaborn
# Carrega um dos datasets que vem com o Seaborn
dados = sea.load_dataset("tips")
dados.head()

# O método joinplot cria um plot de 2 variáveis com gráficos bivariados e univariados
sea.joinplot(data=dados, x="total_bill", y="tip", kind="reg")

# O método lmplot() cria plot com dados e modelos de regressão
sea.lmplot(data=dados, x="total_bill", y="tip", col="smoker")

# Construindo um dataframe com Pandas
df = pd.Dataframe()

# Alimentando o Dataframe com valores aleatórios
df["idade"] = random.sample(range(20, 100), 30)
df["peso"] = random.sample(range(55, 150), 30)
df.shape()
df.head()

#%%
# cada linha abaixo é um modelo de gráfico
# lmplot
sea.lmplot(data=df, x="idade", y="peso", fit_reg=True)

# kdeplot
sea.kdeplot(df.idade)

# kdeplot
sea.kdeplot(df.peso)

# diplot
sea.displot(df.peso)

# Histograma
plt.hist(df.idade, alpha=.3)
sea.rugplot(df.idade)

