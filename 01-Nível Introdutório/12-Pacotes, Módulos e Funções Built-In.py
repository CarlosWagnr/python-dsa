#%%
# Em Python, um módulo é um arquivo (script) que contém código Python e pode ser importado em outros arquivos Python. Ele é usado para compartilhar funções , classes e variáveis entre arquivos.
# Já um pacote é uma coleçãode módulos organizados em uma estrutura de diretórios. Ele permite a divisão de um aplicativo em múltiplos módulos, o que facilita a manutenção e o desenvolviemnto do código.
# Importando um pacote Python
import numpy

# Verificando todos os métodos e atributos disponíveis no pacote
print(dir(numpy))

# Usando um dos métodos do pacote Numpy
numpy.sqrt(25)

# %%
# Importando apenas um dos métodos do pacote Numpy
from numpy import sqrt

# usando o módulo
print(sqrt(9))

# help do método sqrt do pacote Numpy
help(sqrt)

# %%
import random

print("Escolhendo aleatóriamente um item da lista:",random.choice(['Abacate', 'Banana', 'Laranja']))
print("Escolhendo aleatóriamente 10 números entre 1 e 100 ", random.sample(range(100), 10))

# %%
# pacote statistics
import statistics

dados = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]

print("A média dos valores da lista é:", statistics.mean(dados))
print("A mediana dos valores da lista é:", statistics.median(dados))

# %%
import os

print("Qual o diretório do arquivo: ", os.getcwd())
print("Todos os conteúdos do pacote os:\n",dir(os))

# %%
# Importando o módulo request do pacote urllib, usado para trazer url´s
import urllib.request

# variável resposta armazena o objeto de conexão com a url passada como parâmetro.
resposta = urllib.request.urlopen('https://www.python.org/')

# objeto da resposta
print(resposta)

# Chamando o método read() do objeto resposta e armazena o código html na variável html
html = resposta.read()

print(html)

# %%
# Função Map - A função map em Python é uma função que aplica uma determinada função a cada elemento de uma estrutura de dados iterável (como listas, tuplas ou outro objeto iterável.
# A função map retorna um objeto que pode ser convertido em outra estrutura de dados, como lista, se necessário.

# Função python que retorna um número ao quadrado
def potencia(x):
    return x ** 2

numeros = [1, 2, 3, 4, 5]
numeros_ao_quadrado = list(map(potencia, numeros))

print(numeros_ao_quadrado)

# %%
# Criando duas funções

# Função 1 - recebe uma temperatura como parâmetro e retorna a temperatura em Fahrenheit
def fahrenheit(t):
    return ((float(9) / 5) * t + 32)

# Função 2 -recebe uma temperatura como parâmetro e retorna a temperatura em Celsius
def celsius(t):
    return (float(5) / 9) * (t - 32)

# Criando uma lista
temperaturas = [0, 22.5, 40, 100]

# Aplicando a função a cada elemento da lista de temperaturas.
# Em Python 3, a função map retorna um iterator
print("Fahrenheit", list(map(fahrenheit, temperaturas)))

# Usando um loop para imprimir o resultado da função map()
for temp in map(fahrenheit, temperaturas):
    print(temp)

print("Celsius: ", list(map(celsius, temperaturas)))
# %%
# Somando os elementos de duas listas
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

print("Somando elementos", list(map(lambda x, y: x + y, a, b)))
# %%
# Função Reduce - A função reduce() em Python é uma função da biblioteca functools que aplica uma determinada função binária e pares consecutivos de elementos em uma estrutura de dados iterável (como lista, tupla ou outro objeto iterável), reduzindo a um único valor.
# importando a função reduce do módulo functools
from functools import reduce
lista = [47, 11, 42, 13]

# função
def soma(a, b):
    x = a + b
    return x

print("A soma dos valores da lista é:", reduce(soma, lista))

# Usando a função reduce() com lambda
print("A soma dos valores da lista é:",reduce(lambda x, y: x + y, lista))

# Podemos atribuir a expressão lambda a uma variável
max_find = lambda a, b: a if (a > b) else b

# Reduzindo a lista até o valor máximo, através da função criada com a expressão lambda
print("Buscando o maior valor da lista: ",reduce(max_find, lista))

# %%
# Função Filter
# A função filter() em Python é uma função que filtra elementos de uma estrutura de dados iterável (como lista, tupla ou outro objeto iterável) com base em uma determinada condição. A função filter() retorna um objeto filtro, que pode ser convertido em outra estrutura de dados, como uma lista se necessário.

# Criando uma função
def verificaPar(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
lista1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

print("Retorna apenas o números pares da lista:\n",tuple((filter(verificaPar, lista1))))
# %%
# Função Zip
# A função zip() é uma função que agrupa elementos de múltiplas estruturas de dados iteráveis (como lista, tupla ou outros objetos iteráveis) juntos em pares.
# A função zip() retorna um objeto zip, que pode ser convertido em outra estrutura de dados, como uma lista ou dicionário, se necessário.

# Criando duas listas
x = [1, 2, 3]
y = [4, 5, 6]

# Unindo as listas. Em Python retorna um iterável.
# Perceba que zip retorna tuplas.
print("Unindo as listas:", tuple(zip(x, y)))

# Atenção quando as sequências tiverem número diferentes de elementos
print("", tuple(zip("ABCD", "xy")))

# %%
# Função Enumerate
# A função enumerate() em Python é uma função que permite iterar sobre uma estrutura de dados (como lista, tupla ou outro objeto iterável).
# A função da enumerate() retorna um objeto enumerado, que pode ser usado em loops para percorrer a estrutura de dados e acesar o contador e o valor de cada elemento.
seq = ['a', 'b', 'c']
print(tuple(enumerate(seq)))
print()

lista_tecnologia = ['Marketing', 'Tecnologia', 'Business']
for i, v in enumerate(lista_tecnologia):
    print("Tecnologia:", i, v)

print()
for i, v in enumerate('Data Science Academy'):
    print(i, v)

# %%
