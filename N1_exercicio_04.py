"""
Expliquei o que é decorator e padrões de projeto. Crie um decorator que mostre
o tempo de execução de uma função que soma 4 números aleatórios. (2,0)
"""
import datetime
from random import randint
import time


def operacoes(dados):

  def meu_metodo():
    print("Tempo inicial de processo: ", datetime.datetime.now())
    print("Iniciando programa de operacoes...")
    time.sleep(2)
    dados()
    print("Finalizando processo.")
    print("Tempo final de processo: ", datetime.datetime.now())

  return meu_metodo

@operacoes
def cria_dados():
  cadeia_num = []
  for n in range(4):
    cadeia_num.append(randint(0,1000))
  print("A soma dos 4 números é igual a: ", sum(cadeia_num))

cria_dados()