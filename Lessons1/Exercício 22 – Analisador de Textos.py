# Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome: '))

nome1 = nome.replace(" ","")
nome2 = nome.split()
nome3 = len(nome2[0])

print(f'Seu nome tem {len(nome1)} letras')
print(f'Seu nome só com letras maiúsculas: {nome.upper()} ')
print(f'Seu nome só com letras minúsculas: {nome.lower()} ')
print(f'Apenas o seu nome tem: {nome3} letras')

