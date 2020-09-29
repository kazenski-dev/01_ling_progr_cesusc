"""
Escreva um algoritmo que solicita ao usuário para digitar um número inteiro positivo,
e mostre-o por extenso. Este número deverá variar entre 1 e 5. Se o usuário introduzir
um número que não pertença a este intervalo, mostre a frase “número inválido”.
(modifique para calcular tudo no mesmo método, somando
1 ao resultado de cada operação)
"""
class EscreverValor:

  def mostrar_valor (self, valor):
    if valor == 1:
      print("Um")
    elif valor == 2:
      print("Dois")
    elif valor == 3:
      print("Tres")
    elif valor == 4:
      print("Quatro")
    elif valor == 5:
      print("Cinco")
    else:
      print("Numero invalido")

mostra_numero = EscreverValor()

numero = int(input ("Insira um numero positivo e inteiro: "))

mostra_numero.mostrar_valor(numero)

