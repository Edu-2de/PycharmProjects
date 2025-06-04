import random

#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.


tupla = tuple(random.sample(range(50), 20))

print(tupla)
print(f'O maior numero é {max(tupla)}')
print(f'O menor numero é {min(tupla)}')
