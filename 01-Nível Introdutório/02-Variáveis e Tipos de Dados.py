#%%
# Operadores Aritméticos
soma = 4 + 4
subtracao = 7 - 3
multiplicacao = 5 * 2
divisao = 3 / 2
potencia = 4 ** 2
modulo = 10 % 3
divisao_inteiro = 7 // 3
print(f"O valor da soma é: {soma}.\nO tipo de dado da soma é {type(soma)}")

# %%
# Conversão de Dados - float(), int(), str(), hex(), bin()
reais = 10
idade = 32.0
print(float(reais))

# %%
# Funções abs() retorna o valor absoluto, round() arredonda um valor, pow() potência
print("O valor absoluto de -8 é:", abs(-8)) 
print("O valor arredondado de pi é:", round(3.14151922,2))
print("4 elevado a potência 2 é:", pow(4,2))

# %%
# Declaração Múltipla de variáveis
time1, time2, time3 = "Vasco", "Santos", "Internacional"
print(time3)

fruta1 = fruta2 = fruta3 = "Melancia"
print(fruta1)


# %%
# Variáveis Atribuídas a Outras Variáveis e Ordem dos Operadores
largura = 2
altura = 4
area = largura * altura
print(f"O cálculo da área é: {area}")

# %%
# A Ordem dos Operadores é a mesma seguida na Matemática
perimetro = 2 * (largura + 2) * altura
print(f"O perímetro é igual a: {perimetro}")

# %%
# Concatenação de Variáveis
nome = "Carlos"
sobrenome = "Wagner"
fullName = nome + " " + sobrenome
print(fullName)

# %%
# Imprimindo Strings com Formatação Definida.
print("""
    Python
    SQL
    Spark
    Cloud
""")

# %%
# Indexando Strings
s = 'Data Science Academy'
print(s)
print("Primeiro elemento da String:", s[0]) # índice 0
print("Primeiro elemento da String:", s[5]) # índice 5

# %%
# Podemos usar um ":" para executar um slicing que faz a leitura de tudo até um ponto designado.
print("Retorna todos os elementos da string, começando pela posição até o fim da string:", s[1::])

print("Retorna tudo até a posição 3:", s[:3])
print("Indexação negativa e ler de trás para frente:", s[-1])
print("Retorna tudo exceto a última letra:", s[:-1])
print("Retorna saltando de dois em dois caracteres:", s[::2])

print("Podemos usar o símbolo de múltiplicação para criar repetição:", 'w' * 3)

# %%
# Funções Built-in de Strings - upper() caracteres em maiúsculo, lower() caracteres em minúsculo, split() divide a string
dsa = "Data Science Academy é a melhor maneira de estar se preparando para o mercado de trabalho em Ciência de Dados."
print(dsa.split())


# %%
# Funções Strings - capitalize(), count(), isalnum(), islower, isspace(), endwith()
saudacao = 'seja bem vindo ao universo da Linguagem Python!'
print(saudacao)

print(f"Quantas letras 'a' tem na string: {saudacao.count('a')}")

# %%
# Comparando Strings
print("Python == R:", "Python" == "R")
print("Python == Python:", "Python" == "Python")

