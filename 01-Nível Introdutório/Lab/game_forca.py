# Projeto 1 - Desenvolvimento de Game em Linguagem Python - Versão 1

# importando pacotes
import random
from os import system, name

# Função para limpar a tela a cada execução
def limpa_tela():

    # Windows - nt é o nome dado para sistemas Windows.  _ não retorna nada
    if name == 'nt':
        _ = system('cls')

    # Mac ou Linux
    else:
        _ = system('clear')


# Função que desenha a forca na tela
def display_hangman(chances):
    
    # Lista de estágios da forca
    stages = [ # estágio 6 (final)
    """
        --------
        |       |
        |       O
        |      \\|/
        |       |
        |      /\\
        -
    """,
    # estágio 5
    """
        --------
        |       |
        |       O
        |      \\|/
        |       |
        |      /
        -
    """,
    # estágio 4
    """
        --------
        |       |
        |       O
        |      \\|/
        |       |
        | 
        -
    """,
    # estágio 3
    """
        --------
        |       |
        |       O
        |      \\|/
        | 
        |
        -
    """,
    # estágio 2
    """
        --------
        |       |
        |       O
        |      \\
        |  
        | 
        -
    """,
    # estágio 1
    """
        --------
        |       |
        |       O
        | 
        |   
        |  
        -
    """,
    # estágio 0
    """
        --------
        |       |
        |
        |
        |
        |
        -
    """,
    ]
    return stages[chances]

# Função
def game():
    limpa_tela()

    print("\nBem-vindo(a) ao jogo da Forca!")
    print("Adivinhe a palavra abaixo:\n")

    # Lista de palavras para o jogo
    palavras = ["banana", "abacate", "uva", "morango", "laranja"]

    # Escolhe randomicamente uma palavra
    palavra = random.choice(palavras)

    # Lista de letras da palavra
    lista_letras_palavras = [letra for letra in palavra]

    # Cria tabuleiro com caracter "_" multiplicando pelo comprimento da palavra
    tabuleiro = ["_"] * len(palavra)

    # Número de chances
    chances = 6

    # Lista para as letras digitadas
    letras_tentativas = []

    # Loop enquanto o número de chances for maior do que zero
    while chances > 0:
        print(display_hangman(chances))
        print("Palavra: ", tabuleiro)
        print("\n")

        # Tentaiva
        tentativa = input("\nDigite uma letra: ").lower()

        # Condicional
        if tentativa in letras_tentativas:
            print("Você já tentou essa letra. Escolha outra!")
            continue

        letras_tentativas.append(tentativa)

        # Condicional
        if tentativa in lista_letras_palavras:
            print("Você acertou a letra!")
        
            # Loop
            for indice in range(len(lista_letras_palavras)):
                # Condicional
                if lista_letras_palavras[indice] == tentativa:
                    tabuleiro[indice] = tentativa
        
            # Se todos os espaõs foram preenchidos, o jogo acabou
            if "_" not in tabuleiro:
                print("\nVocê venceu, a palavra era:", palavra)
                break

        else:
            print("Ops. Esta letra não está na palavra!")
            chances -= 1


    # Condicional
    if "_" in tabuleiro:
        print("\nVocê perdeu, a palavra era", palavra)


# Bloco main
if __name__ == "__main__":
    game()
    print("\nParabéns! Você está aprendendo Python com a DSA. :)!\n")