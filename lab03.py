from palavras import palavras


def titulo(msg):
  print('-'*100)
  print(f'{msg:^110}')
  print('-'*100)

  
titulo('\033[31mH A N G M A N\033[m')

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

print(forca.get(1))
letras_certas = list()
letras_erradas = list()
sorteio = palavras()
print(len(sorteio), 'letras\n')
print('_ '*len(sorteio))
c1 = 2
c2 = 0
while True:
  chute = str(input('\nChute uma letra: '))
  if chute in sorteio:
    print('\n\033[32mAcertou\033[m\n')
    letras_certas.append(chute)
    for letra in sorteio:
      if letra in letras_certas:
        print('\033[33m',letra,'\033[m' , end='')
      else:
        print(' _ ', end='')
    print()
    # Faltou descobrir como fazer a contagem das letras já descobertas e igualar elas com o tamanho da palavra. Problema: letras repetidas.
    if len(letras_certas) == len(sorteio):
      print(f'\033[32mParabéns!! Você ganhou!\033[m')
      break
  else: 
    print(f'\n\033[31mLetra {chute} não está na palavra.\033[m')
    letras_erradas.append(chute)
    print(forca.get(c1))
    c1 += 1
    for letra in sorteio:
      if letra in letras_certas:
        print('\033[33m',letra,'\033[m' , end='')
      else:
        print(' _ ', end='')
    print()
  if c1 == 8:
    print(f'\033[31mVocê perdeu.\033[m\nA palavra era \033[32m{sorteio}\033[m.')
    print('Mais sorte na próxima vez.')
    break
  print('\nLetras corretas: ', end='')
  print(*letras_certas)
  print('Letras incorretas: ', end='')
  print(*letras_erradas)
    