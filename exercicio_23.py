"""
23 - Crie uma programa que recebe uma lista qualquer e:
a. retorne o maior elemento
b. retorne a soma dos elementos
c. retorne o número de ocorrências do primeiro elemento da lista
d. retorne a média dos elementos.
"""

#Variables
lista = []
media = 0
contador = 0
cont_ocorrencia = 1
cont = 0

#Main Code

print("Vamos criar uma lista de 5 numeros inteiros. \n")

while cont <= 4:
    valor = int(input("Digite um número: {0}:".format(cont + 1)))
    lista.append(valor)
    cont += 1

media = (sum(lista) / 5)

for i in lista:
    if valor == lista[0]:
        cont_ocorrencia += 1

print("Maior valor = ", (max(lista)))
print("Soma dos valores = ", (sum(lista)))
print("Numero de ocorrencias do primeiro elemento = ", cont_ocorrencia)
print("Media dos valores = ", media)
