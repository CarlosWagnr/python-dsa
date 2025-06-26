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

