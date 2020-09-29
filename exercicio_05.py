"""
Ler um valor e escrever se é positivo ou negativo (considere o valor zero como
positivo) Modifique para saber se é par ou ímpar
"""
class PositivoNegativo:

  def valida_numero (self, valor):
    if valor >= 0:
      print("O valor {0} e Positivo".format(valor))
    else:
      print("O valor {0} e Negativo".format(valor))
    if valor % 2 ==0:
      print("Valor {0} e par".format(valor))
    else:
      print("Valor {0} e impar.".format(valor))

teste = PositivoNegativo()

numero = int(input("Insira o numero: "))

teste.valida_numero(numero)