"""
24 - Receba duas listas e exiba a união destas listas e a intercalação destas listas, isto
é, 1º da 1ª lista, 1º da 2ª lista, 2º da 1ª lista, 2º da 2ª lista.
"""

#Variables
lista = []
lista_2 = []
lista_master = []
contador = 3

#Main Code
print("Vamos criar duas listas de 3 numeros inteiros cada. \nLISTA 1:\n")
for n in range(contador):
    lista.append(int(input("Digite um número para adicioná-lo à lista 1: ")))

print("\nLISTA 2:\n")
for n in range(contador):
    lista_2.append(int(input("Digite um número para adicioná-lo à lista 2: ")))

for a, b in zip(lista, lista_2):
    lista_master.append(a)
    lista_master.append(b)

for w in lista_master:
    print(w)
