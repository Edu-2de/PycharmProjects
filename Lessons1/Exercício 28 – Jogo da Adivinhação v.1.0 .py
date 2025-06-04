#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
from time import sleep
print('\033[0;33m-=-' *20)
print('\033[0;34mVou pensar em um núnero de 0 a 5, tente adivinhar!')
print('\033[0;33m-=-' *20)

numeros = (0,1,2,3,4,5)
numero_aleatorio = random.choice(numeros)

usuario = int(input('\033[0;0mEm qual número eu pensei? '))
print('\033[0;35mPROCESSANDO...')
sleep(3)
if usuario == numero_aleatorio:
    print('\033[0;32mVoce acertou!, parábens VOCE GANHOU!!')
else:
    print(f'\033[0;31mVoce errou! Eu GANHEI,tinha pensado no número: {numero_aleatorio}')
