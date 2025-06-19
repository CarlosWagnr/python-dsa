#%%
# Expressão Lambda
potencia = lambda num: num ** 2
potencia(5)

# %%
# Lembrete: Operadores de comparação retornam boolean: True or False
par = lambda x: x % 2 == 0
par(7)

# %%
# Função lambda para pegar a primeira string
first = lambda s: s[0]
first("Python")

# %%
# Função lambda para soma
somaNum = lambda num1, num2: num1 + num2
somaNum(8, 7)

# %%
# List Comprehension - [expressão for item in interable if condição == True]
lista_numero = [x for x in range(11)]
print(lista_numero)

# %%
# List Comprehension que imprime os números menores que 5 em um intervalo de 1 a 10.
lista_numeros = [x for x in range(1, 11) if x < 5]
print(lista_numeros)

# %%
# List Comprehension para buscar as palavras com a letra 'm'
lista_frutas = ["banana", "abacate", "melancia", "cereja", "manga"]

nova_lista = [x for x in lista_frutas if "m" in x]
print(nova_lista)

# %%
# Dict Comprehension
dict_alunos = {'Bob': 68, 'Michel': 84, 'Zico': 57, 'Ana': 93}

# Criamos um novo dicionário imprimindo os pares de chave:valor
dict_alunos_status = {k:v for (k,v) in dict_alunos.items()}
print(dict_alunos_status)

# Criamos um novo dicionário com o status: nota maior que 70, aprovado, senão, reprovado
dict_alunos_status = {k:('Aprovado' if v > 70 else 'Reprovado') for (k,v) in dict_alunos.items()}
print(dict_alunos_status)

# %%
