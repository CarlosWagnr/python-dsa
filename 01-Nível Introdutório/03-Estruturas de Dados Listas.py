#%%
# Trabalhando com Listas com elementos independentes
lista_1 = ["arroz", "feijão", "tomate", "farinha"]
print(lista_1)

# Trabalhando com Listas com elementos separados por vírgula
lista_2 = ["arroz, feijão, tomate, farinha"]
print(lista_2)

lista_3 = [23, 100, "Cientista de Dados"]
print(lista_3)

# Atribuindo cada valor da lista a uma variável
item_1 = lista_3[0]
item_2 = lista_3[1]
item_3 = lista_3[2]
print(item_1, item_2, item_3)

# %%
# Atualizando um item da lista
print(lista_1[2])
lista_1[2] = "chocolate"
print(lista_1[2])

# %%
# Deletando um item da Lista
del lista_1[3]
print(lista_1)

# %%
# Listas de Listas (Listas Aninhadas)
listas = [[1,2,3], [10,15,14], [10,1,8.7,2.3]]
print(listas)

# Atribuindo um item da lista a uma variável
a = listas[0]
print(a)

list1 = listas[1]
print(list1)

# %%
# Operações com Listas
listas = [[1,2,3], [10,15,14], [10,1,8.7,2.3]]
print(listas)

# Atribuindo a uma variável o primeiro valor da primeira lista.
a = listas[0][0]
print(a)

b = listas[1][2]
print(b)

c = listas[0][2] + 10
print(c)

d = 10
e = d * listas[2][0]
print(e)

# %%
# Concatenando Listas
lista_s1 = [34, 32, 56]
lista_s2 = [21, 90, 51]

lista_total = lista_s1 + lista_s2
print(lista_total)

# %%
# Operador in
lista_op = [100, 2, -5, 3.4]

print("O número 10 está na lista:", 10 in lista_op)

# %%
# Funções Built-in - len() tamanho da lista, max() maior valor, min() menor valor, append() adiciona elemento, count() conta elementos
lista_numeros = [10, 2, 50, -3.4]
min(lista_numeros)

lista_formacoes = ["Analista de Dados", "Cientista de Dados", "Engenheiro de Dados"]
lista_formacoes.append("Engenheiro de IA")
print(lista_formacoes)

# %%
# Copiando os itens de uma lista para outra
old_list = [1, 2, 5, 10]
new_list= []


for item in old_list:
    new_list.append(item)
print(new_list)

# %%
# Extendendo uma lista adicionando elementos
cidades = ["Belém", "São Luis", "Manaus"]
cidades.extend(["Rio de Janeiro", "Florianópolis"])
print(cidades)
cidades.index("Manaus")

# Inserindo elemento em um índice da lista
cidades.insert(2, 110)
print(cidades)

# Remove um item da lista
cidades.remove(110)
print(cidades)

# Reverse a lista
cidades.reverse()
print(cidades)

# Organiza a lista de forma alfabética
cidades.sort()
print(cidades)

# %%
