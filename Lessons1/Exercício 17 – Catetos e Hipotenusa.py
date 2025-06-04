import math

# Faca um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre o comprimento da hipotenusa.

cateto_op = int(input('Digite o cateto oposto: '))
cateto_ad = int(input('Digite o cateto adjacente: '))

print('A hipotenusa é: {:.2f}'.format(math.hypot(cateto_op,cateto_ad)))