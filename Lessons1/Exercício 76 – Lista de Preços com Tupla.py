#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos_precos = (('Lápis', 1.75), ('Borracha', 2.00), ('Caderno', 15.90), ('Estojo', 25.00), ('Tranferidor', 4.20), ('Compasso', 9.99), ('MOchila', 120.32))

print('-'*20)
print(' LISTAGEM DE PRECOS')
print('-'*20)
for produto, preco in produtos_precos:
    print(f'{produto}', end=' ')
    print('.'*20, end=' ')
    print(f'{preco}')