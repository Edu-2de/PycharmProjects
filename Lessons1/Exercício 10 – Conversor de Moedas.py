# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considerando U$$1.00 = R$3.27

dinheiro = float(input('Quanto dinheiro voce tem?R$ '))

print('Já que voce tem {:.2f} reias, voce pode comprar {:.2f} dólares'.format(dinheiro, dinheiro/3.27))
