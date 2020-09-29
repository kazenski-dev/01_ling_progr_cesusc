import datetime

def operacoes(dados):

  def meu_metodo():
    print("Tempo inicial de processo: ", datetime.datetime.now())
    print("Iniciando programa de operacoes...")
    dados()
    print("Finalizando processo.")
    print("Tempo final de processo: ", datetime.datetime.now())

  return meu_metodo

@operacoes
def captura_dados():
  numero = int(input("Insira o 1º numero: "))
  numero2 = int(input("Insira o 2º numero: "))

  print("Acabou captura, sao os numeros:  ", numero, numero2)

captura_dados()
