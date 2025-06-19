#%%
# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) 
# e depois faça uma chamada à função para listar os números
def NumPar():
    num = range(1, 21)
    for i in num:
        if i % 2 == 0:
            print(i)

NumPar()

# %%
# Exercício 2 - Crie uam função que receba uma string como argumento e retorne a mesma string em letras maiúsculas.
# Faça uma chamada à função, passando como parâmetro uma string
def UpperString(string):
    return string.upper()

UpperString("Data Science Academy")

# %%
# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e 
# imprima a lista
def adiciona(lista):
    print(lista.append(22))
    print(lista.append(31))
    
lista = [2, 5, 7, 40]
adiciona(lista)
print(lista)


# %%
# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas 
# à função, com apenas 1 elemento e na segunda chamada com 4 elementos
def formal(nome, *elemento):
    print(nome)
    for i in elemento:
        print(i)


formal("Carlos Wagner")
print("*" * 40)
formal("Joaquim", 30, "Setembro", 2023)

# %%
# Exercício 5 - Crie uma função anônima e atribua seu retorno a uma variável chamada soma. A expressão vai receber 2 
# números como parâmetro e retornar a soma deles
soma = lambda num1, num2: num1 + num2
print("A soma é:", soma(5, 9))

# %%
# Exercício 6 - Execute o código abaixo e certifique-se que compreende a diferença entre variável global e local
total = 0
def soma(arg1, arg2):
    total = arg1 + arg2; 
    print ("Dentro da função o total é: ", total)
    return total


soma(10, 20)
print ("Fora da função o total é: ", total)

# %%
## Exercício 7 - Abaixo você encontra uma lista com temperaturas em graus Celsius
# Crie uma função anônima que converta cada temperatura para Fahrenheit
# Dica: para conseguir realizar este exercício, você deve criar sua função lambda, dentro de uma função 
# (que será estudada no próximo capítulo). Isso permite aplicar sua função a cada elemento da lista
# Como descobrir a fórmula matemática que converte de Celsius para Fahrenheit? Pesquise!!!
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda f: ((f * 9) / 5) + 32, Celsius)
print (list(Fahrenheit))


# %%
# Exercício 8 - Crie uma list comprehension que imprima o quadrado dos números de 1 a 10
quadrado = [x**2 for x in range(1,11)]
print(quadrado)


# %%
# Exercício 9 - Crie uma list comprehension que imprima as palavras com a letra a no nome
palavras = ["maça", "coiote", "banana", "terreno", "Python"]
imprime_palavra = [p for p in palavras if 'a' in p]
print(imprime_palavra)

# %%
# Exercício 10 - Crie uma list comprehension que imprima os números menores que 5 em um intervalo de 1 a 10
imprime_numeros = [n for n in range(1, 11) if n < 5]
print(imprime_numeros)

# %%
