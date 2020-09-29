"""
Darth Vader achou que seu exército de stormtrooper estava prendendo poucos
rebeldes, então lhe contratou para desenvolver um programa que leia um conjunto
indeterminado de número de refém presos por mês. Ao final da listagem informe o
menor e o maior número de capturados, a média e o valor mais próximo a média (não
utilize funções prontas do python). (2,0)
"""
import time

lista_refens = []
num_refens = 0
soma = 0
menor = 999
maior = 0
contador = 0
media = 0

while num_refens != -1:
    try:
        num_refens = int(input("Insira o numero de refens... \nOu digite '-1' para sair:"))

        if num_refens != -1:

            lista_refens.append(num_refens)

            if num_refens < menor:
                menor = num_refens
            if num_refens > maior:
                maior = num_refens
            soma += num_refens
            contador += 1
        else:
            print("\nFinalizando programa...")
            time.sleep(2)
            print("\nFinalizado com sucesso.\nObrigado por usar nosso software.")

    except(ValueError):
        print("Favor Insira somente números válidos: (inteiros)")

media = sum(lista_refens)/contador
aux_media = int(media)
print(aux_media)

print("\nMédia da lista: ", media)
print("\nO maior valor é: ", maior)
print("\nO menor valor é: ", menor)

for i in num_refens:
    if num_refens[i] < aux_media:
        aux = menor
        while aux <= aux_media:
            if aux >= aux_media:
                ideal = aux
            aux += 1
    if num_refens[i] > aux_media:
        aux = maior
        while aux <= aux_media:
            if aux >= aux_media:
                ideal = aux
            aux -= 1

print("\nValor mais próximo: ", ideal)

