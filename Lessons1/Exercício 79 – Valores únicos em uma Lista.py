#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista = []
for i in range(15):
    numero = int(input('Digite um numero: '))
    if numero not in lista:
        lista.append(numero)
    else:
        print('Esse numero ja tem na lista')

lista.sort()  # Ordena a lista
print(lista)  # Imprime a lista já ordenada
