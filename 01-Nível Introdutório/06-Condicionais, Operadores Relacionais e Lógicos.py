#%%
# Condicionais - if... elif e else para validar mais de uma condição
dia = "Segunda"

if dia == "Segunda":
    print("Hoje fará sol!")
elif dia == "Terça":
    print("Hoje vai chover")
else:
    print("Sem previsão do tempo para o dia selecionado!")

# %%
# Operadores Relacionais - retorna um booleano True ou False
print("6 é maior do que 3?", 6 > 3)
print("3 é maior do que 7?", 3 > 7)
print("4 é menor do que 8?", 4 < 8)
print("4 é maior ou igual a 4?", 4 >= 4)

if 5 == 5:
    print("Testando Python.")

if True:
    print("Parece que Python funciona")

# %%
# Condicionais Aninhadas
idade = 18
nome = "Bob"

if idade > 13:
    if nome == "Bob":
        print("Ok, Bob, você está autorizado a entrar!")
    else:
        print("Desculpe, mas você não pode entrar!")

idade = 13
nome = "Bob"
if idade >= 13 and nome == "Bob":
        print("Ok, Bob, você está autorizado a entrar!")

# %%
# Operadores Lógicos - and, or e not
numero = 4

if (numero > 5) and (numero % 2 == 0):
    print("Isso está sendo impresso porque as duas consições são verdadeiras!")
else:
    print("Isso está sendo impresso porque uma das duas consições é falsa!")

# %%
# Usando mais de uma condição na cláusula if e introduzindo Placeholders
disciplina = "Data Science"
nota_final = 90
semestre = 2

if disciplina == "Data Science" and nota_final >=80 and semestre != 1:
    print(f"Você foi aprovado em {disciplina} com média final de {nota_final:.1f}!")
else:
    print("Lamento, acho que você precisa estudar mais!")

