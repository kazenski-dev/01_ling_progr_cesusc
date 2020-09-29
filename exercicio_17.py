"""
17 - Cria uma lista para armazenar 5 nomes fixos. Após inserir os 5 nome da lista
mostre-os no console (utilize um for).
"""

#Variables
nomes = []

#Main Code
for i in range(5):
    nome = input("Insira o nome: ")
    nomes.append(nome)
print("\nImpressao do conjunto de nomes:\n")
for i in range(5):
    print(nomes[i])