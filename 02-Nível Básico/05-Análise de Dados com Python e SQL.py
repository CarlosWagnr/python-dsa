#%%
import sqlite3
import pandas as pd
print("Versão do SQLite: ", sqlite3.sqlite_version)
print("Versão do Pandas: ", pd.__version__)

# %%
# Conectando no Banco de Dado =s com Linguagem Python
con = sqlite3.connect("cap12_dsa.db")

# Abre um cursosr para percorrer os dados no banco de dados
cursor = con.cursor()

# Query SQL para extrair os nomes das colunas do banco de dados
sql_query = """SELECT name FROM sqlite_master WHERE type = 'table';"""

# Executa a query
cursor.execute(sql_query)

# Visualiza o resultado
print(cursor.fetchall())


# %%
# Cria uma instrução SQL
query1 = "SELECT * FROM tb_vendas_dsa"
cursor.execute(query1)

# List comprehension para visualizar os nomes das colunas
nomes_colunas = [description[0] for description in cursor.description]
print(nomes_colunas)

dados = cursor.fetchall()

# Visualiza os dados
print(dados)

# %%
# Cria uma instrução SQL para calcular a média de unidades vendidas
query2 = "SELECT AVG(Unidades_Vendidas) FROM tb_vendas_dsa"

# Executa a query
cursor.execute(query2)

# Visualiza os dados
print(cursor.fetchall())


# %%
# Cria uma instrução SQL para calcular a média de unidade vendidas por produto
query3 = "SELECT Nome_Produto, AVG(Unidades_Vendidas) FROM tb_vendas_dsa GROUP BY Nome_Produto"

# Executa a query
cursor.execute(query3)

# Visualiza os dados
print(cursor.fetchall())


# %%
# Cria uma instrução SQL para calcular a média de unidades vendidas por produto, quando o valor unitário for maior que 199
query4 = "SELECT Nome_Produto, AVG(Unidades_Vendidas) FROM tb_vendas_dsa WHERE Valor_Unitario > 199 GROUP BY Nome_Produto"

# Executa a query
cursor.execute(query4)

# Visualiza os dados
print(cursor.fetchall())


# %%
# Cria uma instrução SQL para calcular a média de unidades vendidas por produto, quando o valor unitário for maior que 199, mas somente se a média de unidades vendidas for maior que 10. No SQL a agregação é feita depois do Group BY.
query5 = """SELECT Nome_Produto, AVG(Unidades_Vendidas) 
            FROM tb_vendas_dsa 
            WHERE Valor_Unitario > 199 
            GROUP BY Nome_Produto
            HAVING AVG(Unidades_Vendidas) > 10"""

# Executa a query
cursor.execute(query5)

# Visualiza os dados
print(cursor.fetchall())

# Fecha o cursor e encerra a conexão
cursor.close()
con.close()

# %%
# Aplicando linguagem SQL na Sintaxe do Pandas com Linguagem Python
# Conectando no Banco de Dado =s com Linguagem Python
con = sqlite3.connect("cap12_dsa.db")

# Abre um cursosr para percorrer os dados no banco de dados
cursor = con.cursor()

# Cria uma instrução SQL
query = "SELECT * FROM tb_vendas_dsa"
cursor.execute(query)
dados = cursor.fetchall()

# Criando o DataFrame
df = pd.DataFrame(dados, columns=["ID_Pedido", "ID_Cliente", "Nome_Produto", "Valor_Unitario", "Unidades_Vendidas", "Custo"])

# Exibindo as primeiras linhas do DataFrame
df.head()

# %%
# Fecha o cursor e encerra a conexão
cursor.close()
con.close()

# %%
# Calcula a média de unidades vendidas
media_unidades_vendidas = df["Unidades_Vendidas"].mean()
print("A média de unidades vendidas é:", media_unidades_vendidas)


# %%
# Calcula a média de unidades vendidas por produto
media_unidades_vendidas_por_produto = df.groupby("Nome_Produto")["Unidades_Vendidas"].mean()
media_unidades_vendidas_por_produto.head()

# %%
# Calcula a média de unidades vendidas por produto se o valor uitário for maior do que 199
df[df["Valor_Unitario"] > 199].groupby("Nome_Produto")["Unidades_Vendidas"].mean()


# %%
# Calcula a média de unidades vendidas por produto se o valor uitário for maior do que 199 e somente se a média de unidades vendidas for maior do que 10
#Alternativa A
df[df["Valor_Unitario"] > 199].groupby("Nome_Produto").filter(lambda x: x["Unidades_Vendidas"].mean() > 10)

# %%
#Alternativa B
df[df["Valor_Unitario"] > 199].groupby("Nome_Produto") \
                              .filter(lambda x: x["Unidades_Vendidas"].mean() > 10) \
                              .groupby("Nome_Produto")["Unidades_Vendidas"].mean()

# %%
# Sintaxe SQL X Sintaxe Pandas
# As duas instruções abaixo retornam o mesmo resultado!
# Sintaxe SQL
query5 = """SELECT Nome_Produto, AVG(Unidades_Vendidas) 
            FROM tb_vendas_dsa 
            WHERE Valor_Unitario > 199 
            GROUP BY Nome_Produto
            HAVING AVG(Unidades_Vendidas) > 10"""

# Sintaxe Pandas
df[df["Valor_Unitario"] > 199].groupby("Nome_Produto").filter(lambda x: x["Unidades_Vendidas"].mean() > 10)

# %%
