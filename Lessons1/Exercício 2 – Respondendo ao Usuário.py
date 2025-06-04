# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.


# O (input) serve para que o usuário tenha interacao com o comando, além de usarmos o (str) para indicar que, oque vai ser dito é do tipo (string), ou seja, um texto.

nome = str(input('Qual seu nome? '))

print('Prazer {}, seja muito bem vindo(a)'.format(nome))
