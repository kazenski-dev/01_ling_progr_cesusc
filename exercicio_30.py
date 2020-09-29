"""
30 - Crie um dict com 5 nomes e idades, crie um segundo dict duplicando os itens.
"""
import copy

#Variables
nome_idade = {'Eduardo': 29, 'Murilo': 27, 'Alessandra': 30, 'Carlos': 17, 'Ana': 14}
duplicando = {}

#Main Code

duplicando = copy.deepcopy(nome_idade)
print(duplicando)

