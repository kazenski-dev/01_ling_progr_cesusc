"""
12 - Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior
deles.
"""

#Variables
numero = int(input("Insira o primeiro numero: "))
numero2 = int(input("Insira o segundo numero: "))

#Main Code
if numero > numero2:
    print("O maior valor e: ", numero)
else:
    print("O maior valor e: ", numero2)