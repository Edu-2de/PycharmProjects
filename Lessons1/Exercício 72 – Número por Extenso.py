#Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

tupla = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez",
"onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito",
"dezenove", "vinte")


while True:
    try:
        usuario = int(input('Digite um numero de 0 a 20: '))
        if usuario < 0 or usuario > 20:
            print('Digite somente numeros de 0 a 20')
        else:
            print(f'Voce digitou {tupla[usuario]}')
            break
    except:
        print('Voce fez algo errado')
