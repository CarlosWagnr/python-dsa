#%%
# Expressões Regulares são padrões usados para combinar ou encontrar ocorrências de sequências de caracteres em uma strings. Em Python, expressões regulares são geralmente usadas para manipular strings e realizar tarefas como validação de entrada de dados, extração de informação de strings e substituição de texto.
# Em Python, as Expressões Regulares são suportadas pelo pacote re.
import re

texto = "Meu e-mail é usuarios@hotmail.com e você pode me contatar em usuario2@yahoo.com"

# Expressão regular para contar quantas vezes o caractere @ aparece no texto
resultado = len(re.findall("@", texto))
print(f"O caracter '@' apareceu {resultado} vezes no texto")

# %%
# Expressão regular para extrair a palavra que aparece após a palavra "você" em um texto
resultado = re.findall(r"você (\w+)", texto)
print(f"A palavra após 'você' é: {resultado[0]}")

# Nota: O 'r' antes da string que representa a expressão regular em Python é usado para indicar que é uma string é uma string literal raw. Isso significa que as barras invertidas não são interpretadas como caracteres de escape, mas são incluídas na expressão como parte do padrão.

# %%
# Expressão regular para extrair endereços de e-mails de uma string.
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", texto)

print(emails)

# %%
# Extrair os advébios da frase (sufixo = mente)
text = "O aluno estava incrivelmente perdido, mas encontrou a DSA e rapidamente começou a aprender."

for m in re.finditer(r"\w+mente\b", text):
    print("%02d-%02d: %s " % (m.start(), m.end(), m.group(0)))

# %%
# Regex com ChatGPT
# Variável do tipo string
musica = '''
Todos os dias quando acordo
Não tenho mais
O tempo que passou
Mas tenho muito tempo
Temos todo o tempo do mundo
Todos os dias
Antes de dormir
Lembro e esqueço
Como foi o dia
Sempre em frente
Não temos tempo a perder
Nosso suor sagrado
É bem mais belo
Que esse sangue amargo
E tão sério
E selvagem! Selvagem!
Selvagem!
Veja o sol
Dessa manhã tão cinza
A tempestade que chega
É da cor dos teus olhos
Castanhos
Então me abraça forte
E diz mais uma vez
Que já estamos
Distantes de tudo
Temos nosso próprio tempo
Temos nosso próprio tempo
Temos nosso próprio tempo
Não tenho medo do escuro
Mas deixe as luzes
Acesas agora
O que foi escondido
É o que se escondeu
E o que foi prometido
Ninguém prometeu
Nem foi tempo perdido
Somos tão jovens
Tão jovens! Tão jovens!'''

# %%
# 1- Crie um REGEX para contar quantas vezes o caracter "a" aparece em todo o texto da música.
ocorrencias = re.findall(r'a', musica)
#ocorrencias = len(re.findall(r'a', musica))

# Contando o número de ocorrências
quantidade = len(ocorrencias)

print(f"O caractere 'a' aparece {quantidade} vezes no texto.")

# %%
# 2- Crie um REGEX em Python para contar quantas vezes a palavra "tempo" aparece na música.
ocorrencias = re.findall(r'\btempo\b', musica)

# Contando o número de ocorrências
quantidade = len(ocorrencias)

print(f"A palavra 'tempo' aparece {quantidade} vezes no texto.")

# %%
# 3- Crie um REGEX em Python para para extrair as palavras seguidas por exclamação.
# Usando expressão regular para encontrar todas as palavras seguidas por exclamação
match = re.findall(r'\b\w+!', musica)

print("As palavras seguidas por exclamação são:", match)

# %%
# 4- Crie um REGEX que extrai qualquer palavra cujo antecessor seja a palavra "esse" e o sucessor "amargo".
# Usando expressão regular para encontrar todas as palavras que atendem ao padrão
palavras = re.findall(r'(?<=\besse\s)\w+(?=\samargo\b)', musica)

print(palavras[0])

# %%
# 5- Crie um REGEX que retorne as palavras com acento, mas somente os caracteres na palavra que são anteriores ao caracter com acento.
# Usando expressão regular para encontrar os caracteres antes de um caractere acentuado
caracteres = re.findall(r'\b[\wÀ-ÿ]+[áéíóúãõç]', musica)

print(", ".join(caracteres))

# %%
