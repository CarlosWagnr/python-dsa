#%%
# Abrindo o arquivo para leitura
arq1 = open("arquivos/arquivo1.txt", "r")

# Lendo arquivo
print(arq1.read())

# Contar o número de caracteres
print(arq1.tell())

# Retornar para o início do arquivo
print(arq1.seek(0,0))

# Lendo os primeiros 23 caracteres
print(arq1.read(23))

# %%
# Gravando arquivos
arq2 = open("arquivos/arquivo2.txt", "w")

# Gravando arquivo
arq2.write("Aprendendo a programar em Python")

# Fechando o arquivo
arq2.close()

# Lendo o arquivo gravado
arq2 = open("arquivos/arquivo2.txt", "r")
print(arq2.read())

# %%
# Acrescentando conteúdo
arq2 = open("arquivos/arquivo2.txt", "a")
arq2.write(" E a metodologia da Data Science Academy facilita o aprendizado.")

# Fechando o arquivo
arq2.close()

# Lendo o arquivo gravado
arq2 = open("arquivos/arquivo2.txt", "r")
print(arq2.read())

# Retornar para o início do arquivo
arq2.seek(0,0)


# %%
# Abrindo Dataset em Linha Única
f = open("arquivos/salarios.csv", "r")
data = f.read()
rows = data.split("\n")
print(rows)

# %%
# Dividindo um arquivo em colunas
f = open("arquivos/salarios.csv", "r")
data = f.read()
rows = data.split("\n")
full_data = []

for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)

print(full_data)

# %%
# Contando as Linhas de Um Arquivo
contador = 0
for i in full_data:
    contador += 1

print("O número de linhas é igual a:", contador)

## Contando o Número de Colunas de Um Arquivo
contagem = 0
for row in full_data[0]:
    contagem += 1
    
print(f"O número de colunas do arquivo é {contagem}")

# %%
# Importando arquivos com Pandas
import pandas as pd
print("Versão do Pandas:", pd.__version__)

arquivo = "arquivos/salarios.csv"
df = pd.read_csv(arquivo)
df.head()


# %%
df["Position Title"].value_counts()
# %%
