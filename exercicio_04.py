"""
Faça um programa que receba um valor que é o valor pago, um segundo valor que
é o preço do produto e retorne o troco a ser dado.
(modifique para receber um valor de
desconto e subtraia do valor do produto)

class Troco:

  def valida_troco (self, valor1, valor2):
    if valor1 > valor2:
      print("Troco = R$", valor1 - valor2)
    else:
      print("Valor que falta = R$ ", -(valor1 - valor2))

calculando = Troco()

valor_pago = int(input ("Insira o valor pago: R$ "))
preco_produto = int(input ("Insira o valor do produto: R$ "))

calculando.valida_troco(valor_pago, preco_produto)

"""

class Troco:

  def valida_troco (self, dinheiro, preco):
    total = preco - desconto
    if dinheiro > total:
      print("Troco = R$", dinheiro - total)
    else:
      print("Valor que falta = R$ -", (total - dinheiro))

calculando = Troco()

valor_pago = int(input ("Insira o valor pago: R$ "))
preco_produto = int(input ("Insira o valor do produto: R$ "))
desconto = float(input("Insira o valor do desconto: R$ "))

calculando.valida_troco(valor_pago, preco_produto)
