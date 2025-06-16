#%%
# Loop For
list_strings = ["Data", "Science", "Academy"]
for i in list_strings:
    print(i)

# Imprimindo os valores no intervalo entre 0 e 5 (exclusive)
for item in range(0, 5):
    print(item)

# %%
# Imprimindo os números pares da lista de números
list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in list_num:
    if num % 2 == 0:
        print(num)

# %%
# Strings também são sequências
for caracter in "Python":
    print(caracter)

# %%
# Loop For Aninhado
lista1 = [0, 1, 2, 3, 4]
lista2 = [1, 2, 3]

# Loop externo
for elemento_lista1 in lista1:
    
    #Loop interno
    for elemento_lista2 in lista2:
        print("\n", elemento_lista1 * elemento_lista2)
    
    print("----")

# %%
# O número 47 aparece nas duas listas?
list1 = [10, 16, 24, 39, 47]
list2 = [32, 89, 47, 76, 12]

# Loop externo
for elemento_list1 in list1:
    
    #Loop interno
    for elemento_list2 in list2:
        
        # Condicional
        if elemento_list1 == 47 and elemento_list2 == 47:
            print("O número 47 foi encontrado nas duas listas!")

# %%
# Some os números pares da primeira lista com os números pares da segunda lista
list1 = [10, 16, 24, 39, 47]
list2 = [32, 89, 47, 76, 12]
soma = 0

# Loop externo
for lista in [list1, list2]:
    
    # Loop interno
    for num in lista:
        
        # Condicional
        if num % 2 == 0:
            soma += num

print("A soma dos números pares das duas listas é igual a:", soma)

# Listas podem ser concatenadas em Python
print(list1 + list2)

# %%
# Loop em lista de listas (matrizes) para encontrar o maior número
matriz = [[42, 23, 34], 
          [100, 215, 114], 
          [10.1, 98.7, 12.3]]
maior_numero = 0

#Loop externo
for linha in matriz:
    
    #Loop interno
    for num in linha:
        
        # Condicional
        if num > maior_numero:
            maior_numero = num
print("Maior número: ", maior_numero)

# %%
# Listando as chaves de um dicionário
dict = {"k1":"Python", "k2":"R", "k3":"Scala"}
for k, v in dict.items():
    print(k, v)

# %%
# Loop While
valor = 0
while valor < 10:
    print("Número:", valor)
    valor += 1
else:
    print("Loop concluído!")
print(valor)

# %%
# Pass, Break, Continue
# Se encontrarmos o número 4 interrompemos o loop
valor = 0
while valor < 10:
    if valor == 4:
        break
    else:
        pass
    print(valor)
    valor += 1

# %%
# Desconsideramos a letra z ao imprimir os caracteres da frase
for letra in "Python é zzz incrível!":
    if letra == "z":
        continue
    print(letra)

# %%
# Encontrando números primos entre 2 e 30 usando loop for e while

# Variável para armazenar números primos
primos = []

# Loop for para percorrer números de 2 a 30
for num in range(2, 31):
    
    # variavel controle
    eh_primo = True
    
    # loop while para verificar se o número é primo
    i = 2
    while i <= num // 2:
        if num % i == 0:
            eh_primo = False
            break
        i += 1
    
    # Adicionando o número primo a lista
    if eh_primo:
        primos.append(num)
        
# Imprimindo a lista de números
print(primos)
# %%
