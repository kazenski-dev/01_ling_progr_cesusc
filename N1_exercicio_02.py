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
    nome = ""
    idade = 0
    salario = 0.0

    def aumenta_salario(aumento):
        salario_novo = Funcionario.salario + aumento
        return  salario_novo

    class Programador:
        valor_aumento = 20
        aumenta_salario(valor_aumento)

class Analista:
    valor_aumento = 30
    Funcionario.aumenta_salario(valor_aumento)


print(Programador.conta)
print(Programador.salario)
print(Analista.salario)