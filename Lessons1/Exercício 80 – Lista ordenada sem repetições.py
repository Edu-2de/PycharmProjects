#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.lista = []
lista = []
for i in range(5):
    numero = int(input('Digite um numero: '))

    # Insere o número na lista de forma ordenada
    inserido = False
    for index, number in enumerate(lista):
        if numero < number:
            lista.insert(index, numero)
            inserido = True
            break

    # Se o número for maior que todos os outros, adiciona ao final
    if not inserido:
        lista.append(numero)

print(lista)