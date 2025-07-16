#%%
# Matplotlib é uma biblioteca de visualização de dados em Python amplamente utilizada para criar gráficos e visualizações de alta qualidade em diversas áreas. Ele é compatível com vários formatos de arquivos de imagens permitindo a geração de imagens de alta qualidade para uso em publicações e apresentações.
# ppip install matplotlib
import matplotlib as mpl
mpl.__version__

# %%
# Construindo Plots.
# Plot é uma representação gráfica de dados em figura, é um gráfico que mostra a relação entre duas ou mais variáveis. Um plot pode ser criado usando uma biblioteca de visualização de dados como o Matplotlib em Python.
# Os tipos mais comum incluem gráficos de linhas, dispersão, histogramas e gráficos de barras. Um gráfico de linhas é útil para visualizar tendências em uma série temporal, enquanto um gráfico de dispersão é útil para mostrar a dispersão entre duas variáveis.

# O matplotlib.pyplot é uma coleção de funções e estilos do Matplotlib
import matplotlib.pyplot as plt
#matplotlib inline
# O método plot() define os eixos do gráfico
#plt.plot([1, 2, 5], [2, 4, 7])

x = [2, 3, 5]
y = [3, 5, 7]
plt.plot(x, y)
plt.xlabel('Variável 1')
plt.ylabel('Variável 2')
plt.title('Teste Plot')
plt.show()

#
x2 = [1, 2, 3]
y2 = [11, 12, 15]
plt.plot(x2, y2, label = 'Gráfico coom Matplotlib')
plt.legend()
plt.show()

# %%
# Criando Gráficos de Barras
# Usados para representar dados categórios com barras retangulares. Cada barra representa uma categoria e a altura da barra representa a quantidade ou frequência da categoria.
# O eixo horizontal do gráfico de barras mostra as categorias e o eixo vertical mostra a escala de medida dos dados. As barras podem ser vertical ou horizontal, dependendo da preferência do usuário.
x1 = [2, 4, 6, 8, 10]
y1 = [6, 7, 8, 2, 4]

plt.bar(x1, y1, label="Barras", color="green")
plt.legend()
plt.show()

# Adicionando 2 gráficos na mesma barra de plotagem
x2 = [1, 3, 5, 7, 9]
y2 = [7, 8, 2, 4, 2]

plt.bar(x1, y1, label="Listas 1", color="blue")
plt.bar(x2, y2, label='Listas 2', color="red")
plt.legend()
plt.show()

#
idades = [22, 65, 45, 55, 21, 22, 34, 42, 41, 4, 99, 101, 120, 122, 130, 111, 115, 80, 75, 54, 44, 64, 13, 18, 48]
ids = [x for x in range(len(idades))]
print(ids)
plt.bar(ids, idades)
plt.show()

# histograma em barra
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]
plt.hist(idades, bins, histtype="bar", rwidth=0.8)
plt.show()

# preenche os intervalos entre cada barra.
plt.hist(idades, bins, histtype="stepfilled", rwidth=0.8)
plt.show()

# %%
# Gráfico de Dispersão
# Conhecido como gráfico de pontos, é utilizado para representar a relação entre duas variáveis continuas. Cada ponto no gráfico de dispersão representa um par de valores das duas variáveis, onde uma variável é plotada no eixo horizontal e outra no vertical.
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 2, 4, 5, 6, 8, 4, 8]
plt.scatter(x, y, label="Pontos", color="black", marker='o')
plt.legend()
plt.show()

# %%
# Gráfico de àrea Empilhada
# Usados para visualizar a mudança relativa de diversas variáveis ao longo do tempo. Eles consistem em várias áreas coloridas empilhadas umas sobre as outras, onde a altura representa a magnitude da variável correspondnete e a largura representa a escala de tempo.
dias = [1, 2, 3, 4, 5]
dormir = [7, 8, 6, 77, 7]
comer = [2, 3, 4, 5, 3]
trabalhar = [7, 8, 7, 2, 2]
passear = [ 8, 5, 7, 8, 13]

plt.stackplot(dias, dormir, comer, trabalhar, passear, colors=["m", "c", "r", "k", "b"])
plt.show()

# %%
# Gráfico de Pizza
# Representa um círculo dividido em fatias que representa as proporções relativas das categorias.
horas = [7, 2, 3, 9]
atividades = ["dormir", "comer", "estudar", "trabalhar"]
cores = ["olive", "lime", "violet", "royalblue"]

plt.pie(horas, labels=atividades, colors=cores, startangle=90, shadow=True, explode=(0, 0.2, 0, 0))
plt.show()

# %%
# Criando Gráficos Customizados com Pylab
# Pylab é um módulo fornecido pela biblioteca Matplotlib que combina a funcionalidade do pacote Numpy com a funcionalidade do pacote pyplot. O módulo inclui muitas funções úteis para plotagem de gráficos, como funções para criar gráficos de linha, dispersão, barras, pizza, histograma e muito mais.
from pylab import *

# Gráfico de Linha - Usado para representar a evolução de um comportamento de uma variável com diferentes pontos de dados. São usados para visualizar tendências e padrões em dados contínuos ao longo do tempo.
x = linspace(0, 5, 10)
y = x ** 2

fig = plt.figure()
axes = fig.add_axes([0, 0, 0.8, 0.8])

axes.plot(x, y, "r")
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title("Gráfico de Linha")


# %%
# Histograma - Utilizado para visualizar a distribuição de uma variável contínua. Eles são compostos por barras retângulares adjacentes, onde a área de cada barra é proporcional à frequência de observações de dados que caem em uma faixa específica de valores.
#import numpy as np
n = np.random.randn(100000)
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Plot 1
axes[0].hist(n)
axes[0].set_title("Histograma Padrão")
axes[0].set_xlim((min(n), max(n)))

# Plot 2
axes[1].hist(n, cumulative=True, bins=50)
axes[1].set_title("Histograma Cumulativo")
axes[1].set_xlim((min(n), max(n)))

