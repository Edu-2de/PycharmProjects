#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

#A) Quantas vezes apareceu o valor 9.

#B) Em que posição foi digitado o primeiro valor 3.

#C) Quais foram os números pares.

tupla = (int(input('Digite um numero: ')),
int(input('Digite um numero: ')),
int(input('Digite um numero: ')),
int(input('Digite um numero: ')))
print(f'Voce digitou os valores {tupla}')
print(f'O valor 9 apreceu {tupla.count(9)} vezes')
print(f'O valor 3 apreceu na {tupla.index(3)} posicao')
print(f'O valor 3 apreceu na {tupla.index(3)+1} posicao')
print(f'Os valores pareses digitados foram ', end=' ')
for i in tupla:
    if i % 2 == 0:
        print(i, end=' ')

