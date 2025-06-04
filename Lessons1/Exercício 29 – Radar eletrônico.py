#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.


velocidade = int(input('Qual a velocidade atual do carro em km? '))
if velocidade >80:
    print(f'O total a ser pago é de: {(velocidade-80) *7}R$')
print('Tenha um bom dia! Dirija com seguranca!')