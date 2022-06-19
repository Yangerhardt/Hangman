
class Titulo:
    def __init__(self, msg):
        self.msg = msg
        return self.titulo(msg)

    def titulo(self, msg):
        print('-'*100)
        print(f'{msg:^110}')
        print('-'*100)

class Jogo:
    pass
    
    def __init__(self, lista1, lista2):
        self.lista1 = lista1
        self.lista2 = lista2
        
        
    # método para imprimir o status da forca   
    def forca(self, num=1):
        forca = {1: ''' _ _ _ _ _
|         |
|        
|        
|        
| 
''',
2: ''' _ _ _ _ _
|         |
|         O
|        
|        
|
''',
3: ''' _ _ _ _ _
|         |
|         O
|         |
|        
|
''',
4: ''' _ _ _ _ _
|         |
|         O
|        /|
|        
|
''',
5: ''' _ _ _ _ _
|         |
|         O
|        /|\\
|        
|
''', 
6: ''' _ _ _ _ _
|         |
|         O
|        /|\\
|        / 
|
''',
7: ''' _ _ _ _ _
|         |
|         O
|        /|\\
|        / \\
|
'''}
        return print(forca.get(num))

    def sorteio_palavra(self):
        from palavras import palavras
        self.sorteio = palavras()
        print(f'{len(self.sorteio)} letras.')
        self.cont = 1
        self.c1 = 0
        return self.sorteio

    def status_jogo(self):
        print('Letras certas: ', end='')
        print(*self.lista1)
        print('Letras erradas: ', end='')
        print(*self.lista2) 
        print()  

    def chute(self, lista1, lista2):
        while True:
            chute = str(input('\nChute uma letra: ')).lower().strip()[0]
            if chute in self.lista1 or chute in self.lista2:
                print('Letra já chutada, tente novamente.')
            else: 
                break
        if chute in self.sorteio:
            self.lista1.append(chute)
            print('\n\033[32mAcertou!\n\033[m')
            self.forca(self.cont)
            self.status_jogo()
        else:
            self.lista2.append(chute)
            print(f'\nA palavra não possui a letra \033[31m{chute}\033[m.\n')
            self.cont += 1
            self.forca(self.cont)
            self.status_jogo()

    def palavra(self):
        for letra in self.sorteio:
            if letra in self.lista1:
                print('\033[33m',letra,'\033[m', end='')
                self.c1 += 1
            else:
                print('_ ', end='')
        print()
        if self.c1 == len(self.sorteio):
            pass
        else:
            self.c1 = 0

    def finalizar(self):
        if self.cont == 7:
            print(f'\n\033[31mVocê perdeu.\033[m\nA palavra era \033[32m{self.sorteio}\033[m.')
            return True
        elif self.c1 == len(self.sorteio):
            print(f'\033[32m\nParabéns!! Você ganhou!\033[m\n')
            return True
        else:
            pass


letras_certas = list()
letras_erradas = list()
tit = Titulo('\033[31mH A N G M A N\033[m')
jogo = Jogo(letras_certas, letras_erradas)
jogo.forca()
jogo.sorteio_palavra()
jogo.palavra()

while True:
    jogo.chute(letras_certas, letras_erradas)
    jogo.palavra()
    if jogo.finalizar() == True:
        break