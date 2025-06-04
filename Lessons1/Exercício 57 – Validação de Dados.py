 # Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

while True:
    try:
        seq = str(input('Digite seu sexo:'))
        if seq != 'm' and seq != 'f':
            print('M or F')
        elif seq == 'm':
            print('ola menina')
            break
        elif seq == 'f':
            print('ola menino')
            break
    except:
        print('otario')

