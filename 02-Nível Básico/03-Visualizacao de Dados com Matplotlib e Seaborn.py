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
