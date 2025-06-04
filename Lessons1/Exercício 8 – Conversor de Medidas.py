# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

numero = float(input('Digite uma media em metros:  '))

print('{:.1f} em centímetros é: {:.1f}cm e em milímetros é: {:.1f}mm'.format(numero, numero*100, numero*1000))
