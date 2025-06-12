# Fundamentos de Linguagem Python Para Análise de Dados e Data Science

## CONTEÚDO PROGRAMÁTICO:
- Primeiros Passos com a Linguagem Python - Visão Geral, Instalação e ChatGPT
- Linguagem Python Nível Introdutório - Introdução à Lógica de Programação
- Linguagem Python Nível Introdutório - Variáveis, Tipos e Estruturas de Dados
- Linguagem Python Nível Introdutório - Loops, Condicionais, Métodos e Funções
- Linguagem Python Nível Introdutório -Tratamento de Arquivos, Módulos, Pacotes e Funções Built-in
- Linguagem Python Nível Introdutório - Projeto e Avaliação
#
- Linguagem Python Nível Básico - Introdução à Programação Orientada a Objetos
- Linguagem Python Nível Básico - Matemática e Manipulação de Matrizes com Numpy
- Linguagem Python Nível Básico - Manipulação de Dados com Pandas
- Linguagem Python Nível Básico - Visualização de Dados com Matplotlib e Seaborn
- Linguagem Python Nível Básico - Análise de Dados com Python e Linguagem SQL
- Linguagem Python Nível Básico - Projeto e Avaliação
#
- Linguagem Python Nível Intermediário - Análise Estatística com Statsmodels
- Linguagem Python Nível Intermediário - Análise de Séries Temporais em Python
- Linguagem Python Nível Intermediário - Machine Learning com Scikit-Learn
- Linguagem Python Nível Intermediário - Introdução a Deep Learning com TensorFlow
- Linguagem Python Nível Intermediário - Aprendizado Por Reforço [Reinforcement Learning]
- Linguagem Python Nível Intermediário - Projeto e Avaliação

## ABORDAGEM
- Dedicar-se de 4 a 6 horas por semana, em pequenas doses diárias.
- Cada avaliação tem 65 questões com até 3 tentativas.
- Aproveitamento de 70% ou mais para aprovação.

## REQUISITOS DE HARDWARE & SOFTWARE
- Windows (versões 10 e 11, Home e Pro), MacOS e Linux Ubuntu
- Processador Intel Core i5 e 8GB de RAM
- Máquinas com arquitetura de 64 bits
- Anaconda Python e Google Chrome

## ChatGPT
O ChatGPT é um modelo de linguagem desenvolvido pela OpenAI que utiliza inteligência artificial para entender e gerar texto em linguagem natural. Ele é capaz de manter conversas, responder perguntas, e gerar conteúdo escrito em diversos contextos, como assistente virtual, suporte ao cliente e criação de textos.

## Python
Python é uma linguagem de programação de alto nível, interpretada e de propósito geral, conhecida por sua sintaxe simples e legibilidade. É amplamente utilizada em diversas áreas, como desenvolvimento web, ciência de dados, inteligência artificial e automação. Python oferece tipagem dinâmica, uma vasta biblioteca padrão e suporte a múltiplos paradigmas de programação, como orientada a objetos e funcional. Sua grande comunidade e extensas bibliotecas de terceiros a tornam uma escolha popular entre desenvolvedores.

## Gerando Código Python com ChatGPT
1. Gere código Python que crie uma lista com os números entre 1 e 100 e então imprima os números pares, mas somente se o número for divisível por 4.

```
# Criação da lista com números de 1 a 100
numeros = list(range(1, 101))

# Impressão dos números que são pares e divisíveis por 4
for numero in numeros:
    if numero % 2 == 0 and numero % 4 == 0:
        print(numero)

```

### Explicação do Código:
* **list(range(1, 101))**: Gera uma lista contendo os números de 1 a 100.
* **Loop for**: Itera sobre cada número na lista.
* **Verificação**: O código verifica se o número é par (*numero % 2 == 0*) e se é divisível por 4 (*numero % 4 == 0*).
* **print(numero)**: Se as condições forem atendidas, imprime o número.

Ao executar esse código, ele exibirá todos os números entre 1 e 100 que são pares e divisíveis por 4.
