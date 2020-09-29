"""
28- Faça um programa que percorre uma lista e exiba na tela o valor mais próximo da
média dos valores da lista. Exemplo: lista = [2.5, 7.5, 10.0, 4.0] (média = 6.0). Valor
mais próximo da média = 7.5
"""

#Variables
lista = []
contador = 5
media = 0
ideal = 0

#Main Code
for n in range(contador):
    lista.append(int(input("Digite um número para adicioná-lo à lista: ")))

media = (sum(lista)/5)
print("Media = ", media)

lista.sort()
print("Lista ordenada: ", lista)
"""
for i in lista:
    if lista[i] <= media:
            ideal = i
"""

cont = 1
while cont <= len(lista):
    if lista[cont] <= media or lista[cont] >= media:
        ideal = lista[cont]
    cont += 1


print("O valor mais proximo da media e: ", ideal)