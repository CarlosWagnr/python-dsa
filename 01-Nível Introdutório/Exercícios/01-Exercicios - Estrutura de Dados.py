#%%
# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.
lista_numeros = list(range(0, 11))
print(lista_numeros)

# %%
# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
lista_objetos = ["carro", "avião", "moto", "bicicleta", "caminhão"]
print(lista_objetos)

# %%
# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
string1 = "Jesus"
string2 = "Cristo"
juncao_strings = string1 + " " + string2
print(juncao_strings)

# %%
# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla
tupla_numeros = (1, 2, 2, 3, 4, 4, 4, 5)
print("Quantas vezes aparece o número 4?", tupla_numeros.count(4))

# %%
# Exercício 5 - Crie um dicionário vazio e imprima na tela
dicionario_vazio = {}
print(dicionario_vazio)

# %%
# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
dicionario_elementos = {"key01": "Python", "key02": "SQL", "key03": "Spark"}
print(dicionario_elementos)

# %%
# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
dicionario_elementos["key04"] = "Java"
print(dicionario_elementos)

# %%
# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. 
# Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.
dicionario_valores = {"01": 10.99, "02": 23.90, "03": [30.00, 9.99]}
print(dicionario_valores)

# %%
# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dicionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista.
lista_elementos = ["Dados", (30, 55), {"key01": "Engenheiro", "key02": "Cientista"}, 10.55]
print(lista_elementos)

# %%
# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
print(frase[0:18])

# %%
