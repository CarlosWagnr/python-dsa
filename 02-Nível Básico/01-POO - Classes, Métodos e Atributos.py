#%%
# Programação Orientada a Objetos (POO) é um paradigma de programação que se baseia no  conceito  de  "objetos",  que  são  entidades  que  possuem  características  (atributos)  e comportamentos (métodos). Em POO, o foco está na criação de **objetos** que interagem entre si para realizar tarefas.

# A POO tem como princípio a encapsulação, que é a capacidade de um objeto de ocultar seus detalhes internos e expor apenas o necessário para interagir com outros objetos. Além disso, a POO também se baseia em *herança* e polimorfismo, que permitem a reutilização de código e a criação de hierarquias de classes que representam conceitos e objetos mais abstratos.

# Classes - 
# Em programação Orientada a Objetos (POO), uma classe é uma estrutura que descreve um objeto, especificando os atributos e comportamentos que o objeto deve ter. Uma classe é uma espécie de modelo que define as características e ações que um objeto deve possuir.

# As classes são usadas para criar objetos, que são instâncias da classe. Cada objeto criado a partir da mesma classe terá todos os mesmos atributos e comportamentos.

# Para criar uma classe em Python, utiliza-se a palavra reservada class.

# O nome da classe segue a mesma conversão de nomes para criação de funções e variáveis em Python, mas normalmente se usa a primeira letras maiúscula em cada palavra no nome da clase.

class Livro():
    # Este método vai iniciar cada objeto criado a partir desta classe.
    # O nome deste método é __init__, método construtor.
    # (self) é uma referência a cada atributo da própria classe (e não de uma classe mãe, por exemplo)
    def __init__(self):
        
        # Atributos
        self.titulo = "Sapiens - Uma breve História da Humanidade"
        self.isbn = 9988888
        print("Construtor chamado para criar um objeto desta classe.")
    
    # Métodos são funções que executam ações nos objetos da classe.
    def imprime(self):
        print(f"Foi criado o livro {self.titulo} com ISBN {self.isbn}")

# Criando uma instância da classe
Livro1 = Livro()
print(Livro1.titulo)
print(Livro1.isbn)

print(Livro1.imprime())

# %%
# Criando a classe Livro com parâmentros no método construtor.
class Livro():

    def __init__(self, titulo, isbn):
        
        # Atributos
        self.titulo = titulo
        self.isbn = isbn
        print("Construtor chamado para criar um objeto desta classe.")
    
    # Métodos 
    def imprime(self, titulo, isbn):
        print(f"Foi criado o livro {self.titulo} com ISBN {self.isbn}")

# Criando o objeto Livro2 que é uma instância da classe Livro
Livro2 = Livro("O poder do Hábito", 77886611)

Livro2.imprime("O poder do Hábito", 77886611)
print("O Título do livro é:", Livro2.titulo)

# %%
# Criando a classe
class Algoritmo():
    def __init__(self, tipo_algo):
        self.tipo = tipo_algo
        print("Construtor chamado para criar um objeto desta classe.")

carro1 = Algoritmo("VolksWagen")
print("Qual a marca do carro: ", carro1.tipo)

carro2 = Algoritmo("Chevrolet")
print("Qual a marca do carro: ", carro2.tipo)

# %%
# Objetos - Usamos a função type, para verificar o tipo de um objeto.
class Estudante():
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota

# Criando um objeto chamado Estudante1 a partir da classe Estudante
Estudante1 = Estudante("Carlos", 32, 9.5)

# Atributos da classe Estudante, utilizado por cada objeto criado a partir desta classe
print(f"Meu nome é {Estudante1.nome}, tenho {Estudante1.idade} anos e minha nota é {Estudante1.nota}")


# %%
# Criando uma classe Funcionario
class Funcionario():
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
        
    def listFunc(self):
        print(f"Funcionário(a) {self.nome} tem o salário de {self.salario} e o cargo é {self.cargo}")
        
# Criando um objeto chamado Func1, a partir da classe Funcionario
Func1 = Funcionario("Wagner", 7.467, "Engenheiro de Dados")

Func1.listFunc()
print("No objeto Func1 tem o atributo nome?", hasattr(Func1, "nome"))
print("No objeto Func1 tem o atributo salario?", hasattr(Func1, "salario"))
print("Mude o salário do objeto Func1 para 4.500", setattr(Func1, "salario", 8500))
print("No objeto Func1 delete o salário:", getattr(Func1, "salario"))
print("No objeto Func1 tem o atributo nome?", delattr(Func1, "salario"))
print("No objeto Func1 delete o salário:", hasattr(Func1, "salario"))

# %%
# Trabalhando com Métodos, Herança e Polimorfismo
# Em Python, métodos de classes são funções definidas dentro de uma classe, que realizam operações específicas em objetos criados a partir dessa classe. Os métodos de classes são usados para implementar o comportamento dos objetivos que pertecem a essa classe.

# Assim como as funções em Python, os métodos podem receber argumentos e retornar valores. No entanto, diferentemente das funções normais, os métodos de classe sempre incluem o parâmentro self como primeiro argumento, que é usado para se referir ao objeto atual da classe.

# O método init é um método especial que é chamado quando um objeto é criado a partir da classe. Este método é usado para inicializar os atributos do objeto. Outros métodos podem ser definidos para excutar tarefas específicas em um objeto, como calcular valores, realizar operações de entrada e saída, ou alterar o estado do objeto.

class Circulo():
    # O valor de pi é constante
    pi = 3.14
    
    # Quando um objeto desta classe for criado, este método será excutado e o valor default do raio será 5
    def __init__(self, raio = 5):
        self.raio = raio
        
    # Este método calcula a área.
    def area(self):
        return (self.raio * self.raio) * Circulo.pi
    
    # Método para gerar um novo raio
    def setRaio(self, novo_raio):
        self.raio = novo_raio
        
    # Método para obter o raio do círculo
    def getRaio(self):
        return self.raio

# Criando o objeto Circ, uma instância da classe Circulo()
Circ = Circulo()
Circ.raio

# %%
# Criando outro objeto chamado Circ1. Uma instãncia da classe circulo()
# Agora sobreescrevendo o valor do atributo
Circ1 = Circulo(7)

Circ1.raio
Circ1.area()
Circ1.setRaio(9)
Circ1.area()

# Imprimindo o novo raio
print(f"O novo raio é igual a {Circ1.getRaio()}")

# %%
# Herança
# Em Programação Orientada a Objetos (POO), a herança é um concenito que permite criar novas classes a partir de outras classes existentes, aproveitando os atributos e métodos da classe original e adicionando novos atributos e métodos específicos.

# A classe original é chamada de classe mãe ou superclasse e a nova classe criada é chamada de classe filha ou subclasse.

# A herança é uma técnica importante em POO porque permite reutilizar o código de maneira eficiente. Em vez de criar uma nova classe do zero, a subclasse pode herdar todos os atributos e métodos da superclasse e adicionar apenas o que é necessário. Desta forma, a subclasse pode se concentrar em fornecer funcionalidades adicionais sem precisar se preocupar coom as características básicas da classe.

# Na herança, uma subclasse pode herdar os atributos e métodos da superclasse e substituí-los ou estendê-los conforme necessário. Por exemplo, uma subclasse pode ter um método com o mesmo nome da superclasse, mas com comportamento diferente.

# Criando uma classe Animal - Super-classe
class Animal:
    
    def __init__(self):
        print("Animal criado")
    
    def imprimir(self):
        print("Este é um animal")
    
    def comer(self):
        print("Hora de comer!")
        
    def emitir_som(self):
        pass


# %%
# Criando classe Cachorro - Sub-classe da classe Animal
class Cachorro(Animal):
    
    def __init__(self):
        Animal.__init__(self) # Inicia o construtor da super classe
        print("Objeto Cachorro criado!")
        
    def emitir_som(self):
        print("Au au!")

cao = Cachorro()
cao.emitir_som()
cao.comer()

# %%
# Criando classe Gato - Sub-classe
class Gato(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("Objeto Gato criado!")
        
    def emitir_som(self):
        print("Miau!")

cat = Gato()
cat.emitir_som()
cat.imprimir()

# %%
# Polimorfismo
# Polimorfismo é um dos conceitos fundamentais da Programação Orinetada a Objetos (POO). O polimorfismo permite que objetos de diferentes classes possam ser tratados de forma uniforme. Isso significa que um objeto pode ser tratado como se fosse um objeto de uma superclasse, mesmo que ele seja de uma subclasse.

# Mais especificamente, o polimorfismo se refere à habilidade de um objeto responder de diferentes formas a uma mesma mensagem. Isso é possível porque as subclasses podem implementar métodos com o mesmo nome que os métodos da superclasse, mas com comportamentos diferentes.

# Com o polimorfismo, os mesmo atributos e métodos podem ser utilizados em objetos distintos, porém, com implementações lógicas diferentes.

# Superclasse
class Veiculo:
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        pass

    def frear(self):
        pass

# %%
# Subclasse
class Carro(Veiculo):

    def acelerar(self):
        print("O carro está acelerando.")

    def frear(self):
        print("O carro está freando")


# %%
# Subclasse
class Moto(Veiculo):

    def acelerar(self):
        print("A moto está acelerando.")

    def frear(self):
        print("A moto está freando")

# %%
# Subclasse
class Aviao(Veiculo):

    def acelerar(self):
        print("O avião está acelerando.")

    def frear(self):
        print("O avião está freando")

    def decolar(self):
        print("O avião está decolando.")

# %%
# Cria os objetos
lista_veiculos = [Carro("Porshe", "911 Turbo"), Moto("Honda", "CB 1000R Black Edition"), Aviao("Boeing", "757")]

# Loop
for item in lista_veiculos:
    
    # O método acelerar tem comportamento diferente dependendo do tipo do objeto
    item.acelerar()
    
    # O método frear tem comportamento diferente dependendo do tipo do objeto
    item.frear()
    
    # Executando o método decolar somente se o objeto for instância da classe Aviao
    if isinstance(item, Aviao):
        item.decolar()
        
    print("---")

