# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

reta1 = float(input('Digite o comprimeto da reta: '))
reta2= float(input('Digite o comprimeto da reta: '))
reta3 = float(input('Digite o comprimeto da reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('É possível formar o triangulo')
else:
    print('NAO DA PRA FORMAR O TRIANGULO')