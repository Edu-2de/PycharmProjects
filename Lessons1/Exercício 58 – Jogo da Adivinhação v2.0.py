#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random
from time import sleep
print('\033[0;33m-=-' *20)
print('\033[0;34mVou pensar em um núnero de 0 a 5, tente adivinhar!')
print('\033[0;33m-=-' *20)



while True:
    try:
        numeros = (0, 1, 2, 3, 4, 5)
        numero_aleatorio = random.choice(numeros)
        usuario = int(input('\033[0;0mEm qual número eu pensei? '))
        print('\033[0;35mPROCESSANDO...')
        sleep(3)
        if usuario != numero_aleatorio:
            print(f'\033[0;31mVoce errou! Eu GANHEI,tinha pensado no número: {numero_aleatorio}')
    except:
        print('falido')
    if usuario == numero_aleatorio:
        print('\033[0;32mVoce acertou!, parábens VOCE GANHOU!!')
        break








