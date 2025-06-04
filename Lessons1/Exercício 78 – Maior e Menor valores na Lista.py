#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lisa = []
numero1 = int(input('Digite um numero: '))
lisa.append(numero1)
numero2 = int(input('Digite um numero: '))
lisa.append(numero2)
numero3 = int(input('Digite um numero: '))
lisa.append(numero3)
numero4 = int(input('Digite um numero: '))
lisa.append(numero4)
numero5 = int(input('Digite um numero: '))
lisa.append(numero5)

maior = max(lisa)
menor = min(lisa)
print(lisa)
print(maior, lisa.index(maior))
print(menor, lisa.index(menor))

