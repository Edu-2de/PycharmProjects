contador = 1
x = int(input('Quantas vezes: '))
nome=input('Qual o nome: ')
anoNasc= int(input(f'Digite o ano de {nome}: '))
while nome !='FIM':
    print(f'Criatura {nome} tem {2024 - anoNasc} anos')
    print(f' {contador}/{x}')
    nome=input('Qual o nome: ')
    anoNasc= int(input(f'Digite o ano de {nome}: '))
    if contador >= x:
        print('Excesso')
        break
    nome=input('Qual o nome: ')
    anoNasc= int(input(f'Digite o ano de {nome}: '))
    contador+=1
else:
    print('Digitou FIM')
