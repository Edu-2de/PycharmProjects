n = int(input('Digite um númro:'))
maior = n
menor = n
for i in range(9):
    n = int(input('Digite um número: '))
    if n>maior:
        maior=n

    if n<menor:
        menor=n

print(f'O maior é: {maior}')
print(f'O menor é: {menor}')


