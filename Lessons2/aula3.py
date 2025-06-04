# Faça um programa que recebe 10 números e mostre se é par ou impar

contpar=0
contimpar=0

d = int(input('Digite a quantidade de numeros'))


for i in range(0, d):
    h = int(input('Digite um número: '))

    if h % 2 == 0:
        print('é par')
        contpar+=1
    else:
        print('é impár')
        contimpar+=1






print(f"par = {contpar}")
print(f"impar = {contimpar}")
