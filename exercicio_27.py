"""
27 - Duas amigas estabeleceram o código abaixo para que suas mensagens não
fossem lidas pelas demais pessoas.
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
&#39; &#39; a b c d e f g h i j k l m n o p q r s t u v w x y z
Observe que cada letra equivale a um número entre 1 e 26 e o espaço ao 0. Faça um
método para &quot;traduzir&quot;, que recebe uma lista com uma mensagem (secreta) e &quot;traduz&quot;
a sequência armazenada em uma lista.
"""

class Quot:

    def traduzir_quot (self, codigo):

        secreto = {0: " ",1: "a",2: "b",3: "c",4: "d",5: "e",6: "f",7: "g",8: "h",9: "i",10: "j",11: "k",12: "l",13: "m",14: "n",15: "o",16: "p",17: "q",18: "r",19: "s",
                   20: "t",21: "u",22: "v",23: "x",24: "x",25: "y",26: "z"}
        frase = []

        for a in codigo:
            for b, c in secreto.items():
                if codigo[a] == secreto[b]:
                    frase.append(secreto[b])
                else:
                    print("Valor {0} nao encontrado, prosseguindo...".format(codigo[a]))
        print(frase)
#Variables
validar = 0
mensagem = []

#Main Code
while  g!= 999:
    for n in range(3):
        mensagem.append(int(input("Digite um número para adicioná-lo à lista 1: ")))
        validar = int(input("Digite '999' para SAIR e criptografar:"))
        try:
            if validar == 999:
                break
        except (ValueError):
            print("Favor digite um NUMERO.")

envia_comando = Quot()
envia_comando.traduzir_quot(mensagem)
