import math

# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

numero = int(input('Digite um angulo qualquer: '))

print('O cosseno, tangente e seno desse angulo sao: {}. {}. {}'.format(math.cos(numero), math.tan(numero), math.sin(numero)))
