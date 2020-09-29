"""
faça um método que receba um número X e uma palavra no console e repita x vezes a essa frase.
"""
LIMITE = 10

class MostraPalavra:

  def mostrando (self, valor, frase):
    for i in range(valor):
      print(frase)

imprimir = MostraPalavra()

numero = int(input("Insira um numero: "))
palavra = input("Insira uma palavra: ")

imprimir.mostrando(numero, palavra)