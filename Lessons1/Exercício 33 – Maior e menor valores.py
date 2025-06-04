# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

numero1 = int(input('DIGITE UM NÚMERO: '))
numero2 = int(input('DIGITE OUTRO: '))
numero3 = int(input('DIGITE MAIS UM: '))

maior = numero1
if numero1 > numero2 and numero1 > numero3:
    maior = numero1
if numero2 > numero1 and numero2 > numero3:
    maior = numero2
if numero3 > numero2 and numero3 > numero1:
    maior = numero3

print(f'O maior número é {maior}')

menor = numero2
if numero1 < numero2 and numero1 < numero3:
    menor = numero1
if numero2 < numero1 and numero2 < numero3:
    menor = numero2
if numero3 < numero2 and numero3 < numero1:
    menor = numero3

print(f'O menor número é {menor}')