"""
Crie uma classe calculadora com as quatro operações básicas (soma, subtração,
multiplicação e divisão). O usuário deve informar dois números e o programa deve
fazer as quatro operações.
(modifique para calcular tudo no mesmo método, somando
1 ao resultado de cada operação)

class Calculadora:

  def operacoes (self, valor1, valor2):
    print("Soma = ", valor1 + valor2)
    print("Subtracao = ", valor1 - valor2)
    print("Multiplicacao = ", valor1 * valor2)
    print("Divisao = ", valor1 / valor2)

operando = Calculadora()

numero = int(input ("Insira o 1º numero: "))
numero2 = int(input ("Insira o 2º numero: "))

operando.operacoes(numero, numero2)

"""

class Calculadora:

  def operacoes (self, valor1, valor2):

    print("Valor de +1 adicionado aos resultados finais...")

    print("Soma = ", (valor1 + valor2) + 1)
    print("Subtracao = ", (valor1 - valor2) + 1)
    print("Multiplicacao = ", (valor1 * valor2) + 1)
    print("Divisao = ", (valor1 / valor2) + 1)

operando = Calculadora()

numero = int(input ("Insira o 1º numero: "))
numero2 = int(input ("Insira o 2º numero: "))

operando.operacoes(numero, numero2)