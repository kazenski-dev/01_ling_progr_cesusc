"""
receba três notas de um aluno e informe se ele passou ou reprovou.
"""

class ValidaAluno:

    def verifica(self):
        MEDIA = 7
        soma = 0

        for i in range(3):
            nota = int(input("Insira a {0}ª nota: ".format(i + 1)))
            soma += nota

        print("Resultado Final...")
        print("Media Obtida = {0}".format(soma / 3))
        if nota >= MEDIA:
            print("Aluno Aprovado")
        else:
            print("Aluno Reprovado")


imprimir = ValidaAluno()

imprimir.verifica()