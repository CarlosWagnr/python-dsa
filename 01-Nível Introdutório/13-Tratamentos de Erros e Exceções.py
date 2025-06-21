#%%
# Utilizando try, except e else
try:
    f = open("arquivos/testandoerros.txt", 'w')
    f.write("Gravando no arquivo")
except IOError:
    print("Erro: arquivo não encontrado ou não pode ser salvo")
else:
    print("Conteúdo gravado com sucesso!")
    f.close()
finally:
    print("Comandos no bloco finally são sempre executados")

# %%
# Criando função que pede para o usuário digitar um número
def askint():
    try:
        val = int(input("Digite um número inteiro: "))
    except:
        print("Você não digitou um número!")
    finally:
        print("Obrigado")

askint()

# %%
# Criando uma função com loop para tratamento de erro
def askint():
    while True:
        try:
            val = int(input("Digite um número inteiro: "))
        except:
            print("Você não digitou um número!")
            continue
        else:
            print("Obrigado por digitar um número!")
            break
        finally:
            print("Fim da execução!")
        print(val)

askint()

# %%
