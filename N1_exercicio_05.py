"""
Duas amigas estabeleceram o código abaixo para que suas mensagens não
fossem lidas pelas demais pessoas.
0 12 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
' ' a b c d e f g h i j k l m n o p q r s t u v w x y z
Observe que cada letra equivale a um número entre 1 e 26 e o espaço ao 0.
Faça um método para "traduzir", que recebe uma lista com uma mensagem
(secreta) e "traduz" a sequência armazenada em uma lista.
"""
import time
import datetime

def traduzir(codigo, tamanho):

    def limpa_tela():
        print("Limpando histórico...")
        print("\n" * 150)

    def contagem():
        print("3\n\n\n\n")
        time.sleep(1)
        limpa_tela()
        print("2\n\n\n\n")
        time.sleep(1)
        limpa_tela()
        print("1\n\n\n\n")
        time.sleep(1)
        limpa_tela()

    print("\nProcessando dados ...")
    time.sleep(1)

    limpa_tela()

    contagem()

    for i in range(tamanho):
        analise = codigo[i]
        cruzamento = cod_secreto[analise]
        traducao.append(cruzamento)

    print("\nRecodificado.")
    print(''.join(traducao))
    print("\n")
    print("Fim de operacao: ", datetime.datetime.now())


cod_secreto = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
          'v', 'w', 'x', 'y', 'z']
cod_bruto = []
traducao = []
teste = True

print("Inicio de operacao: ", datetime.datetime.now())
print("Sistema de segurança de mensagens ativo.\nInsira o codigo...\n")
while teste == True:
    try:
        mensagem = int(input(">>> "))
        cod_bruto.append(mensagem)
        validar = str(input("Efetuar tradução? 's' - sim"))
        if validar == "s":
            teste = False

    except(ValueError):
        print("Você digitou algum valor inválido.\nReconectando...")
        time.sleep(2)

tam_codigo = len(cod_bruto)

traduzir(cod_bruto, tam_codigo)