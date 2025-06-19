#%%
# Calculadora em Python
from time import sleep
print("{:*^64}".format(" Calculadora em Python "))

print("""
Selecione o número da operação desejada:

1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
""")
sleep(2)

# Funções
def soma(x, y):
    print(f"\n{x} + {y} = {x + y}")

def subtracao(x, y):
    print(f"\n{x} - {y} = {x - y}")

def multiplicacao(x, y):
    print(f"\n{x} * {y} = {x * y}")

def divisao(x, y):
    if x > y:
        print(f"\n{x} / {y} = {x / y}")
    else:
        print("Divisão Inválida")

# Condição para operações
lista_opcoes = [1, 2, 3, 4]
opcao = int(input("Digite a opção (1/2/3/4): "))

if opcao in lista_opcoes:
    num1 = int(input("\nDigite o primeiro número: "))
    num2 = int(input("\nDigite o segundo número: "))
    
    # Condição para chamada das funções
    if opcao == 1:
        soma(num1, num2)
    elif opcao == 2:
        subtracao(num1, num2)
    elif opcao == 3:
        multiplicacao(num1, num2)
    elif opcao == 4:
        divisao(num1, num2)
else:
    print("Opção Inválida!")
# %%
