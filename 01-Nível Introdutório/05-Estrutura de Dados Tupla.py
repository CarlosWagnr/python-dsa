#%%
# Trabalhando com Tuplas - Estrutura Imutável
tupla1 = ("Geografia", 23, "Elefantes", 9.8, 'Python')
print(tupla1)
print(f"Quantos itens tem na tupla: {len(tupla1)}")

tupla1[0]
print("Qual o índex do elemento elefante:", tupla1.index("Elefantes"))

# Deletando a tupla
del tupla1

# %%
# Criando uma tupla
t2 = ('A', 'B', 'C')
print(t2)

# tuplas não suportam atribuição de itens
#t2[0] = 'D'

# %%
# Usando a função list() para converter uma tupla para lista
lista_t2 = list(t2)
print(lista_t2)

lista_t2.append('D')
print(lista_t2)

t2 = tuple(lista_t2)
print(t2)

