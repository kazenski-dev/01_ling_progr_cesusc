"""
Crie um classe Funcionário com os atributos nome, idade e salário. Deve ter
um método aumenta_salario. Crie duas subclasses da classe funcionário,
programador e analista, implementando o método nas duas subclasses. Para
o programador some ao atributo salário mais 20 e ao analista some ao salário
mais 30, mostrando na tela o valor. Depois disso, crie uma classe de testes
instanciando os objetos programador e analista e chame o método
aumenta_salario de cada um.(2,0)
"""

class Funcionario:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.aumento = 0

    def aumenta_salario(self):
        self.salario = self.salario + self.aumento

class Programador(Funcionario):
    def __init__(self, nome, idade, salario):
        Funcionario.__init__(self, nome, idade, salario)
        self.aumento = 20

class Analista(Funcionario):
    def __init__(self, nome, idade, salario):
        Funcionario.__init__(self, nome, idade, salario)
        self.aumento = 30

class Teste(Funcionario):
    def __init__(self, nome, idade, salario):
        Funcionario.__init__(self, nome, idade, salario)
        self.aumento = 90


pessoa_dev = Programador("Eduardo kazenski", 29, 1500)
print("Funcionario: {0}".format(pessoa_dev.nome))
print("Salario normal: {0}".format(pessoa_dev.salario))
pessoa_dev.aumenta_salario()
print("Salario com acrecimo: {0}".format(pessoa_dev.salario))

pessoa_analyst = Analista("Lucicreide", 30, 2500)
print("Funcionario: {0}".format(pessoa_analyst.nome))
print("Salario normal: {0}".format(pessoa_analyst.salario))
pessoa_analyst.aumenta_salario()
print("Salario com acrecimo: {0}".format(pessoa_analyst.salario))

bckp_teste = Teste("pessoa cadastrada", 1, 1)
print("Funcionario: {0}".format(bckp_teste.nome))
print("Salario normal: {0}".format(bckp_teste.salario))
pessoa_analyst.aumenta_salario()
print("Salario com acrecimo: {0}".format(bckp_teste.salario))
