# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preco a pagar, sabendo que custa R$60 por dia e R$0.15 por km rodado.

km = int(input('Qual a quantidade de km percorridos? '))
dias = int(input('Por quantos dias ele foi alugado? '))

print('O total a ser pago é de: {}'.format((dias*60)+(km*0.15)))
