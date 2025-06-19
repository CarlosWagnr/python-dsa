#%%
# Imprime números de 1 a 10
for i in range(1, 11):
    print(i)

# %%
# Usando tamanho de uma lista na função range()
lista = ['Abacaxi', 'Banana', 'Morango', 'Uva']
lista_tamanho = len(lista)
for i in range(0, lista_tamanho):
    print(i)

# %%
# Métodos - Tudo em Python é um objeto. E cada objeto tem métodos e atributos.
lista = [100, -2, 12, 65, 0]
print("Tipo do objeto:", type(lista))

# Usando um método do objeto lista
lista.append(100)
print(lista)

# Usando um método do objeto lista
print("Quantos números 100 tem na lista:", lista.count(100))

# A função help explica como utilizar cada método de um objeto
help(lista.count)

# Cada objeto tem métodos diferentes para cada tipo de objeto.
#dir(lista)

frase = 'Isso é uma string'
# O método de um objeto pode ser chamado dentro de uma função, como print()
print(frase.split())

# %%
# Funções - Bloco de códigos que você pode chamar várias vezes dentro do programa.
def primeriaFunc():
    nome = "Bob"
    print(f"Hello, {nome}!")

primeriaFunc()

# Definindo uma função com parâmetro
def segundaFunc(nome):
    print(f"Hello, {nome}! Seja Bem Vindo!")

segundaFunc("Carlos")

# %%
# Função para somar números
def somaNum(firstnum, secondnum):
    print("Primeiro número: ", str(firstnum))
    print("Segundo número: ", str(secondnum))
    print("Soma: ", firstnum + secondnum)

somaNum(7, 7)

# %%
# Funções com números variável de argumentos
def printVarInfo(arg1, *vartuple ):
    # Imprimindo o valor do primeiro argumento
    print("O parâmetro passado foi: ", arg1)
    
    # Imprimindo o valor do segundo argumento
    for item in vartuple:
        print("O parâmetro passado foi: ", item)
    return

printVarInfo(4, ("Python", 98))
print("*" * 40)
printVarInfo('Data', 'Science', 'Academy')

# %%
# Escopo de Variável - Local e Global
var_global = 10 # Esta é uma variável global

# Função
def multiplicaNumeros(num1, num2):
    var_global = num1 * num2  # Esta é uma variável local
    print(var_global)

multiplicaNumeros(3, 9)
print(var_global)

# %%
# Funções Built-in
print("Tamanho da lista: ", len([23, 34, 45, 56]))
array = [1, 2, 3]
print("Menor número", min(array))
print("Maior número", max(array))
print("A soma do array é igual a: ", sum(array))

# %%
# Criando Funções usando outras Funções
import math

# Verificando se um número é primo
def numPrimo(num):
    if (num % 2) == 0 and num > 2:
        return "Este número não é primo."
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if (num % i) == 0:
            return "Este número não é primo"
    return f"O número {num} é primo"

numPrimo(7)

# Criando função
caixa_baixa = "Este Texto Deveria Estar Todo Em LowerCase"
def lowerCase(texto):
    return texto.lower()

lowerCase(caixa_baixa)

# %%
# Fazendo Split dos Dados
def split_string_palavras(text):
    return text.split(" ")

texto = "Esta função será bastante útil para separar grandes volumes de dados"
split_string_palavras(texto)

# %%
# Fazendo Split dos Dados
def split_string_letras(text):
    texto = text.upper()
    for letra in texto:
        print(letra)

split_string_letras(texto)

# %%
