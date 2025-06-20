#%%
texto = "Cientista de Dados pode ser uma excelente alternativa de carreira.\n"
texto = texto + "Esses profissionais precisam saber como programar em Python.\n"
texto += "E, claro, devem ser profissionais em Data Science."

# Import o módulo os (operation sistem)
import os

# criando um arquivo
arquivo = open(os.path.join("arquivos/cientista.txt"), "w")

# Gravando dados no arquivo
for palavra in texto.split():
    arquivo.write(palavra + ' ')

# Fechando o arquivo
arquivo.close()

# Lendo o arquivo
arquivo = open("arquivos/cientista.txt", "r")
conteudo = arquivo.read()
arquivo.close()
print(conteudo)

# %%
# Usando a expressão with
with open("arquivos/cientista.txt", "r") as arquivo:
    conteudo = arquivo.read()

print("O tamanho do arquivo é igual a:", len(conteudo))
print(conteudo)

with open("arquivos/cientista.txt", "w") as arquivo:
    arquivo.write(texto[:19])
    arquivo.write("\n")
    arquivo.write(texto[28:66])

# Lendo o arquivo
with open("arquivos/cientista.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# %%
# Manipulando Arquivos CSV
import csv # Importando o módulo csv

with open("arquivos/numeros.csv", "w") as arquivo:
    
    # Cria o objeto gravador
    grava_arquivo = csv.writer(arquivo)
    
    # Grava no arquivo linha a linha
    grava_arquivo.writerow(('nota1', 'nota2', 'nota3'))
    grava_arquivo.writerow((63, 87, 92))
    grava_arquivo.writerow((61, 79, 76))
    grava_arquivo.writerow((72, 64, 91))

# Leitura de arquivos csv
with open("arquivos/numeros.csv", "r", encoding='utf8', newline='\r\n') as arquivo:
    leitor = csv.reader(arquivo)
    for x in leitor:
        print(x)

# %%
# Gerando uma lista com dados do arquivo csv
with open("arquivos/numeros.csv", "r", encoding='utf8', newline='\r\n') as arquivo:
    leitor = csv.reader(arquivo)
    dados = list(leitor)
    
print(dados)

# Imprimindo a partir da segunda linha
for linha in dados[1:]:
    print(linha)

# %%
# Manipulando Arquivos Json (Java Object Notation)
dict_guido = {
    "nome": "Guido Van Rossum",
    "linguagem": "Python",
    "similar": ["c", "Modula-3", "lisp"],
    "users": 1000000
}

for k, v in dict_guido.items():
    print(k, " - ", v)

# %%
# Importando o módulo JSON
import json

# Importando o dicionário para um objeto json
json.dumps(dict_guido)

# Criando um arquivo Json
with open("arquivos/dados.json", "w") as arquivo:
    arquivo.write(json.dumps(dict_guido))

# Leitura de arquivos json
with open("arquivos/dados.json", "r") as arquivo:
    texto = arquivo.read()
    dados = json.loads(texto)

print(dados)
print(dados["nome"])

# %%
# Imprimindo um arquivo JSON copiado da internet
from urllib.request import urlopen

response = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')
dados = json.loads(response)[0]

print(dados)
# %%
print("Título: ", dados["title"])
print("URL: ", dados["url"])
print("Duração: ", dados["duration"])
print("Número de Visualizações: ", dados["stats_number_of_plays"])


# %%
# Copiando o conteúdo de um arquivo para outro
arquivo_fonte = "arquivos/dados.json"
arquivo_destino = "arquivos/dados.txt"

# Método 1
with open(arquivo_fonte, "r") as infile:
    texto = infile.read()
    with open(arquivo_destino, "w") as outfile:
        outfile.write(texto)

# Método 2
open(arquivo_destino, "w").write(open(arquivo_fonte, "r").read())

# Leitura do arquivo txt
with open("arquivos/dados.txt", "r") as arquivo:
    texto = arquivo.read()
    dados = json.loads(texto)

print(dados)

# %%
