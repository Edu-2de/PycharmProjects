# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor da sua casa? '))
salario = float(input('Qual seu salário? '))
anos = int(input('Em quantos anos voce terá pag a sua casa? '))

an = anos*12
sal = salario*an
div = casa//an
pocentagem = salario*0.3

if div > pocentagem:
    print('\033[0;31m EMPRÉSTIMO NEGADO!')
else:
    print('\033[0;32m EMPRÉSTIMO ACEITO')