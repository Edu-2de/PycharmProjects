import random

#  Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))

# A (lista) é um elemento fundamental, nela podemos armazenar informacoes que depois serao de valiosa importância, sempre entre []

lista = [aluno1, aluno2, aluno3, aluno4]

print('O aluno sorteado foi: {}'.format(random.choice(lista)))
