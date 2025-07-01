#%%
# Biblioteca Numpy
import numpy as np

print("Versão do Numpy:",np.__version__)

# Criando Arrays Numpy
array1 = np.array([10, 21, 32, 43, 48, 15, 76, 57, 89])
print(type(array1))
print(array1)
print("Verificando o formato do array1:",array1.shape)

# Um array numpy é uma estrutura de dados multidimensional usada em computação e análise de dados. O array fornece um objeto de matriz N-dimensional (ou ndarray), que é uma grade homogênea de elementos, geralmente números, que podem ser indexados por um conjunto de inteiros.

# Os arrays são mais eficientes que as listas para armazenar e manipular grandes quantidades de dados, pois são implementados em Linguagem C e fornecem várias otimizações de desempenhos.

print("\nImprimindo o valor do índice 4 do array:", array1[4])
print("Imprimindo os valores entre os índice 1 e 4 do array:", array1[1:4])

# Criando uma lista de índices
indices = [1, 2, 5, 6]
print("Imprimindo os valores de acordo com os índices:", array1[indices])

# Criando uma máscara booleana para os elementos pares
mask = (array1 % 2 == 0)
print("\nImprimindo soomente os valores pares do array:", array1[mask])

# Alterando um elemento do arra
array1[0] = 100
print(array1)

# Não é permitido incluir elemento de outro tipo
try:
    array1[0] = "Novo elemento"
except:
    print("Operação não permitida!")

# %%
# Funções Numpy
arr2 = np.array([1, 2, 3, 4, 5])
print("Imprime a soma acumulada dos elementos:", arr2.cumsum())
print("Imprime o produto acumulado dos elementos:", arr2.cumprod())

# a função arange cria um array numpy contendo uma progressão aritmética a partir de um intervalo - start, stop, step
arr3 = np.arange(0, 50, 5)
print("\nNovo array criado com a função arange:", arr3)
print("Verificando o formato do array:", arr3.shape)
print("Tipo do array:", arr3.dtype)

# %%
# Criando um array preenchido com zeros
arr4 = np.zeros(10)
print(arr4, "\n")

# Retorna 1 nas posições diagonal e 0 no restante
arr5 = np.eye(3)
print(arr5, "\n")

# Os valores passados como parâmentro, formam uma diagonal
arr6 = np.diag(np.array([1, 2, 3, 4]))
print(arr6, "\n")

# Array de valores booleanos
arr7 = np.diag(np.array([True, False, False, True]))
print(arr7, "\n")

# Array de strings
arr8 = np.array(["Python", "R", "Julia"])
print(arr8, "\n")

# A função linspace() do Numpy é usada para criar uma sequência de números igualmente espaçados dentro de um intervalo específicado.
print(np.linspace(0, 10))

# A função logspace() do Numpy é usada para criar uma sequência de números igualmente espaçados em escala logarítmica dentro de um intervalo especificado.
print(np.logspace(0, 5, 10))

# %%
# Manipulando Matrizes
arr9 = np.array([[1, 2, 3], [4, 5, 6]])
print("Criando um Matriz:\n", arr9)
print("\nVerificando o formato do array:", arr9.shape)

# Criando uma matriz 2x3 apenas com números "1"
arr10 = np.ones((2, 3))
print("Matriz de apenas números '1'.\n", arr10)

# %%
# Listas de listas
lista = [[13, 81, 22], [0, 34, 59], [21, 48, 94]]

# A função 'matrix' cria uma matriz a partir de uma lista de listas
arr11 = np.matrix(lista)
print("\nVerificando o formato do array:", arr11.shape)
print(arr11)

print("\nTamanho da matriz:", arr11.size)

print("Imprimindo os elementos da coluna 1 e índice 2:", arr11[1,2])

# %%
# Forçando a criação da matrix com tipo específico de dados
arr12 = np.array([[24, 76, 92, 14], [47, 35, 89, 2]], dtype=float)
print("Tipo da matrix:", arr12.dtype)
print("Array criado com os dados em float.\n.", arr12)

# %%
# O itemsize de um array numpy é um atributo que retorna um tamanho em byte de cada elemento do array. Em outras palavras, o itemsize representa o número de bytes necessários para armazenar cada valor do array numpy.

print("Tamanho em bytes para armazenar a matrix: ", arr12.itemsize)
print("Tamanho em nbytes para armazenar a matrix: ", arr12.nbytes)
print("Número de dimensões da matrix: ", arr12.ndim)


# %%
# Manipulando objetos de 3 e 4 Dimensões com Numpy
arr_3d = np.array([
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ],
    [
        [13, 14, 15, 16],
        [17, 18, 19, 20],
        [21, 22, 23, 24]
    ]
])

print("Número de dimensões da matrix: ", arr_3d.ndim)
print("\nVerificando o formato do array:", arr_3d.shape)
print(arr_3d)
print("\nDimensão, linha, coluna: [0, 2, 1] =",arr_3d[0, 2, 1])

# %%
# Manipulando Arquivos com Numpy
import os
filename = os.path.join("arquivos/dataset.csv")

# Carregando dataset para dentro de um array de um mesmo tipo
arr13 = np.loadtxt(filename, delimiter=",", usecols=(0, 1, 2, 3), skiprows=1)
print(arr13)

# %%
# Análise Estatística Básica com Numpy
arr14 = np.array([15, 23, 63, 94, 75])

print("A média do array é:", np.mean(arr14))

# O desvio padrão é uma media útil porque permite avaliar a variabilidade dos dados em torno da média. Se os valores estiverem próximos da média, o desvio padrão será baixo, indicando que os dados tem pouca variabilidade. por outro laso, se os valores estiverem muito distantes da média, o desvio padrão poderá ser alto, indicando que os dados tem alta variabilidade.
print("O desvio padrão do array é:", np.std(arr14))

# A variância é uma média estatística que quantifica a dispersão dos valores em um conjunto de dados em relação a média. Ela é calculada com a média dos quadrados das diferenças entre cada valor e a média.
print("A variância do array é:", np.var(arr14))

# Quando Usar Desvio Padrão ou Variância?

# Tanto a variância quanto o desvio padrão são medidas úteis de dispersão e podem ser usados em conjunto para descrever a distribuição de um conjunto de dados.

# Avariância é uma medida quadrática e pode ser útil para calcular outras estatísticas, como o desvio padrão. No entanto, como a variância é uma medida quadrática, seus valores são geralmente maiores do que os valores dos próprios dados, o que pode dificultar a interpretação. O desvio padrão é a raiz quadrada da variância e fornece uma medida de dispersão que tem a mesma unidade de medida que os próprios dados, facilitando a interpretação e a comparação com outros valores.

# Em geral, o desvio padrão é mais comumente usado do que a variância, principalmente porque é mais fácil de interpretar. No entanto, a escolha entre o uso da variância ou do desvio padrão depende do contexto e do objetivo da análise. Em alguns casos, a variância pode ser uma medida  mais  apropriada,  como  quando  se  pretende  calcular  outras  estatísticas,  como  a covariância ou o coeficiente de correlação. Em outros casos, o desvio padrão pode ser uma medida mais apropriada, como quando se pretende avaliar a consistência dos dados em relação à média e comparar diferentes conjuntos de dados

# %%
# Operações Matemáticas com Numpy
arr15 = np.arange(1, 10)

print("Soma dos elementos:", np.sum(arr15))
print("Produto dos elementos:", np.prod(arr15))
print("Soma acumulada dos elementos:", np.cumsum(arr15))

# Cria 2 arrays
arr16 = np.array([3, 2, 1])
arr17 = np.array([1, 2, 3])

# Soma dos arrays
arr18 = np.add(arr16, arr17)
print("Soma dos arrays:", arr18)

# Para multiplicar duas matrizes Numpy, podemos usar a função dot() ou o operador @. Ambos os métodos executam a multiplicação matricial. O número de colunas da primeira matriz deve ser igual ao número de linhas segunda matriz.

# Cria 2 matrizes
arr19 = np.array([[1, 2], [3, 4]])
arr20 = np.array([[5, 6], [0, 7]])
print("Formato do array: linhas, colunas:", arr19.shape)
print("Array 20:\n", arr20)

# Multiplicando as duas matrizes
arr21 = np.dot(arr19, arr20)
print("\nMultiplicação das matrizes:\n", arr21)

# %%
# Slicing (Fatiamento) de Arrays NumPy
arr22 = np.diag(np.arange(3))
print(arr22)
print("Elemento dos índice 1 e 1 =", arr22[1, 1])
print("Linha 1:", arr22[1])
print("Coluna 2:", arr22[:, 2])

arr23 = np.arange(10)
print("\nArray de 10 elementos:", arr23)

# %%
# Cria 2 arrays
a = np.array([1, 2, 3, 4])
b = np.array([4, 2, 2, 4])

print("Comparação item a item: a == b", a == b)
print("Comparação global: a == b", np.array_equal(a, b))
print("Valor máximo do array a:", a.max())

# Somando um valor a cada elemento do array
c = np.array([1, 2, 3]) + 1.5
print("Soma de c com 1.5 = ", c)

arr24 = np.array([2.5, 3.5, 4.5])
arr25 = np.around(arr24)
print("Usando método around:" , arr25)

# %%
# O método flatten() com Numpy é usado para criar uma cópia dimensional (ou achatada) de um array multidimesional. Isso significa que todo método cria um novo array unidimensional, que contém que contém todos os elementos do array multidimensional, mas que está organizado em uma única linha seguindo a ordem dos elementos do array.
arr26 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr26)

# Achatando a matriz
arr27 = arr26.flatten()
print(arr27)

arr28 = np.array([1, 2, 3])
print()
print("Repetindo valores 3 vezes:", np.repeat(arr28, 3))
print("Repetindo os elementos:", np.tile(arr28, 3))

arr29 = np.copy(arr28)
print(arr29)

# %%
