"""
18 - Crie uma classe animal com o método comer, este método deve escrever na tela
&quot;o animal esta comendo&quot;. Depois disso crie as classes cachorro, cavalo e gato e
implemente o método comer de acordo com o que cada animal come. Crie uma classe
AnimalTeste e coloque os três animais dentro de uma lista de animais e chame o
método comer polimorficamente (com um for)
"""

class Animal:

    def Comer(self, comida):
        print("O animal esta comendo ", comida)

class Cachorro:
    Animal.Comer("Osso")

class Gato:
    Animal.Comer("Whisklas Sache")

class Cavalo:
    Animal.Comer("Milho triturado")

class AnimalTeste:

    animais = [Cachorro, Gato, Cavalo]

    for i in range(3):
        print("O que voce come:")
        print(animais[i].Comer)

