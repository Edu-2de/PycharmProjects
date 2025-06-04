# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = int(input('Digite seu salário: R$'))
if salario >= 125:
    print(f'O seu salário teve um aumento de 15%, ficando um total de: R${salario + (salario * 0.15)}')
else:
    print(f'O seu salário teve um aumento de 10%, ficando um total de: R${salario + (salario * 0.10)}')