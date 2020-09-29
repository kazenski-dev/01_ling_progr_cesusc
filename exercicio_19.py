"""
19 - Crie uma classe chamada Bicicleta. Ela terá os seguintes métodos:
quantidadeMarchas(); tipoFreio() e marca(); Crie também duas classes que estendem
esta classe, uma se chamará BicicletaPasseio e a outra BicicletaProfissional. Para
ﬁnalizar crie uma classe onde deverá estar o método main e crie uma instancia de cada
tipo de bicicleta e mostre o resultado dos métodos.
"""

class Bicicleta:
    def quantidadeMarchas(self, quantMarchas):
        print("Bicicleta com {0} marchas.".format(quantMarchas))

    def tipoFreio(self, tipoFreio):
        print("Bicicleta com tipo de freio {0}".format(tipoFreio))

    def marca(self, marca):
        print("Bicicleta da marca {0}".format(marca))

class BicicletaPasseio:
    Bicicleta.quantidadeMarchas()
    Bicicleta.tipoFreio()
    Bicicleta.marca()

class BicicletaProfissional:
    Bicicleta.quantidadeMarchas()
    Bicicleta.tipoFreio()
    Bicicleta.marca()

class Principal:
    Bicicleta.quantidadeMarchas()
    Bicicleta.tipoFreio()
    Bicicleta.marca()

    def main(self):
        tipoBicicleta = Bicicleta()
        tipoBicicleta.marca()