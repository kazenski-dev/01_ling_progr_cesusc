"""
Escreva uma classe que contém um método que calcule se a pessoa é maior de 18
anos ou não. Receba os dados pela console e chame este método.
(modifique este exercício para receber 5 alunos, 3 notas para cada um e
calcule a média mostrando se está aprovado ou não)"""

class ValidaDados:

  def validar_notas (self):

    soma = 0
    media = 0

    for alunos in range(5):

      print("\nAluno {0}".format(alunos + 1))

      for valores in range(3):

        nota = int(input("{0}ª nota: ".format(valores + 1)))
        soma += nota

      media = soma / 3
      print("\nAluno com media = {0}".format(media))

      soma = 0


  def calcula_idade(self):

    idade = int(input("\nInsira a idade: "))

    if idade >= 17:
      print("Maior de Idade")
    else:
      print("Menor de Idade.")



teste_idade = ValidaDados()

teste_idade.validar_notas()

teste_idade.calcula_idade()