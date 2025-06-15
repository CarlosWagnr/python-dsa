#%%
# Trabalhando com Dicionários
estudantes_dict = {"Pedro":24, "Ana":22, "Ronaldo":26, "Janaina":25}
print(estudantes_dict)

# Adicionando um estudante a lista
estudantes_dict["Marcelo"] = 23
print(estudantes_dict["Marcelo"])

# Limpa o Dicionário
estudantes_dict.clear()
print(estudantes_dict)

# Deleta o Dicionário
del estudantes_dict

# %%
# Criando um novo Dicionário
estudantes = {"Pedro":24, "Ana":22, "Ronaldo":26, "Janaina":25}
print(f"Qual a qunatidade de itens do dicionário: {len(estudantes)}")
print(f"Quais as chaves do dicionário: {estudantes.keys()}")
print(f"Quais os valores do dicionário: {estudantes.values()}")

# %%
# Criando outro Dicionário
estudantes2 = {"Camila":27, "Adriana":28, "Roberta":26}
print(estudantes2)

# Atualiza o primeiro dicionário com o segundo e adiciona os objetos.
estudantes.update(estudantes2)
print("Dicionário atualizado: ",estudantes)

# %%
# Criando um dicionário vazio
dict1 = {}

# Adiconando itens no dicionário
dict1["chave_um"]= 2
dict1[10]= 5
print(dict1)

# Limpa o dicionário
dict1 = {}
print(dict1)

dict1["key1"] = "Data Science"
dict1["key2"] = 10
dict1["key3"] = 100
print(dict1)

a = dict1["key1"]
print(a)

# %%
# Dicionários de listas
dict2 = {'chave1':1230, 'chave2':[22, 453, 73.4], 'chave3':['picanha', 'fraldinha', 'alcatra']}
print(dict2)

print(dict2['chave2'])

# Acessando um item da lista dentro do dicionário
print(dict2['chave3'][0].upper())

# Operações com itens da lista, dentro do dicionário
var1 = dict2['chave2'][0] - 2
print(var1)

# Duas operações no mesmo comando, para atualizar um item da lista
dict2['chave2'][0] -=2
print(dict2)

# %%
# Criando Dicionários Aninhados
dict_aninhado = {'key1': {'key2_aninhada':{'key3_aninhada': 'Dict aninhado em Python'}}}
print(dict_aninhado)

dict_aninhado['key1']['key2_aninhada']['key3_aninhada']
