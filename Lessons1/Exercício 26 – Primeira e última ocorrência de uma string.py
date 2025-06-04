# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip()

print(frase.upper().count('A'))
print(frase.upper().find('A')+1)
print(frase.upper().rfind('A')-1)