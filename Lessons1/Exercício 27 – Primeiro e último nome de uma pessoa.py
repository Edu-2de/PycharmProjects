# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
from typing import List

nome = str(input('Digite seu nome: ')).strip()

nome1 = nome.split()

print('O nome 1 é: {}'.format(nome1[0]))
print('O nome 2 é: {}'.format(nome1[len(nome1)-1]))
