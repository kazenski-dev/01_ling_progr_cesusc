"""
16 - Faça um algoritmo que leia os valores de COMPRIMENTO, LARGURA e ALTURA
e apresente o valor do volume de uma caixa retangular. Utilize para o cálculo a fórmula
VOLUME = COMPRIMENTO * LARGURA * ALTURA.
"""

#Variables
comprimento = float(input("Insira o valor do comprimento:"))
largura = float(input("Insira o valor do largura:"))
altura = float(input("Insira o valor do altura:"))

#Main Code
print("O volume e: {0} metros cubicos.".format(comprimento * altura * largura))
