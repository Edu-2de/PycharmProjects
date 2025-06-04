# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

viagem = int(input('Qual foi a distancia da viagem em km? '))
if viagem <= 200:
    print(f'O preco total a ser pago é de: {viagem*0.50}R$')
else:
    print(f'O preco total a ser pago é de: {viagem*0.45}R$')
