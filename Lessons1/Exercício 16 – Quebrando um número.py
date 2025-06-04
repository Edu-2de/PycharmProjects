import math

# Crie um programa que leia um número real qualquer do teclado e mostre na tela a sua porcao inteira.


# Aqui vemos a funcionalidade (import) funcionando, nela podemos importar a biblioteca que quisermos, afim de achar mais comandos para executar.

numero = float(input('Digite um número real: '))

print('A parte inteira do número: {} é: {}'.format(numero, math.trunc(numero)))
