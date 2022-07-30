import random

with open("palavras.txt", "r", encoding='utf8') as arq:
    listPalavras = arq.read().split()


class Jogo:

    desenho = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''',
               '''

+---+
|   |
O   |
    |
    |
    |
=========''',
               '''

+---+
|   |
O   |
|   |
    |
    |
=========''',
               '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''',
               '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''',
               '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''',
               '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

    def __init__(self):
        self.palavra = random.choice(listPalavras)
        self.vidas = 5
        self.palavraRevelada = ''
        self.listPalavraRevelada = []
        self.listaEscondida = []
        self.inicio()

    def inicio(self):
        for x in self.palavra:
            self.palavraRevelada += '_'
            self.listaEscondida.append('_')
            self.listPalavraRevelada.append(x)
        self.printHangman()

    def verificaLetra(self, letra):
        encontrado = 0
        idx = 0

        for ltr in self.palavra:

            if ltr == letra:
                encontrado = 1
                self.listaEscondida[idx] = letra
                self.palavraRevelada = ''
                for x in self.listaEscondida:
                    self.palavraRevelada += x

            else:
                if self.listPalavraRevelada[idx] == '_':
                    self.listPalavraRevelada[idx] = '_'

            idx += 1

        if encontrado == 0:
            self.vidas -= 1

        self.printHangman()

    def printHangman(self):

        if self.vidas < 0:
            self.defeat()

        else:
            if self.palavra == self.palavraRevelada:
                self.won()

            else:
                print("\n" * 20)
                print(self.desenho[5 - self.vidas])
                print("Palavra a ser descoberta: " + self.palavraRevelada)

                self.verificaLetra(input("Insira uma letra: "))

    def won(self):
        print(self.desenho[5 - self.vidas])
        print("Você venceu o jogo")
        print("A palavra era %s" % self.palavra)

    def defeat(self):
        print(self.desenho[6])
        print("Você perdeu")
        print("A palavra correta era: %s" % self.palavra)


jg = Jogo()