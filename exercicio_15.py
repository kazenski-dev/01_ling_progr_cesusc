"""
15 - Ler 10 valores (considere que não serão lidos valores iguais) e escrever o maior
deles.
"""

#Variables
maior = 0

#Main Code
for i in range(10):
    numero = int(input("Insira um numero: "))

    if numero > maior:
        maior = numero

print("O maior valor inserido foi: ", maior)