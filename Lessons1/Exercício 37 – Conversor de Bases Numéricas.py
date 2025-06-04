#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número: '))


print('Escolha uma das bases de convercao: ')
print('[ 1 ] Converter para BINÁRIO')
print('[ 2 ] Converter para OCTAL')
print('[ 3 ] Converter para HEXADECIMAL')

escolha = int(input('SUA OPCAO: '))
if escolha == 1:
    print(f'Seu número em binario é: {bin(num)}')
elif escolha == 2:
    print(f'Seu número em octal é: {oct(num)}')
elif escolha == 3:
    print(f'Seu número em Hexadecimal é: {hex(num)}')
print('POR HOJE É SÓ, OBRIGADO!')



