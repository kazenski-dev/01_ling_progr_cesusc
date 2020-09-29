"""
26 - Faça um programa que receba duas listas e retorne True se são iguais ou False
caso contrário, além do número de ocorrências do primeiro elemento da lista.
"""

#Variables
lista = []
lista_2 = []
contador = 3

#Main Code
print("Vamos criar duas listas de 3 numeros inteiros cada. \nLISTA 1:\n")
for n in range(contador):
    lista.append(int(input("Digite um número para adicioná-lo à lista 1: ")))

print("\nLISTA 2:\n")
for n in range(contador):
    lista_2.append(int(input("Digite um número para adicioná-lo à lista 2: ")))

# lista.count(lista[0])

print("\nVerificacao de igualdade entre as listas... \n ", lista == lista_2)
print("\nOcorrencias do 1º elemento da lista 1: ", lista.count(lista[0]))
print("\nOcorrencias do 1º elemento da lista 2: ", lista_2.count(lista[0]))