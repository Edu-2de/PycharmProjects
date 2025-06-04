# Desenvolva um programa que leia duas notas de um aluno, calcule e mostre sua média


# Usa (float()) aqui por conta de nao se tratarem de números inteiros, e sim notas, que tem variacoes

nota1 = float(input('Digite a primeria nota: '))
nota2 = float(input('Digite a segunda nota: '))

# Nesse (print()) afim de fazer a média, colocamos a soma dentro de outros parenteses, para que ela seja feita primeiro, e depois a divisao

print('A média total é: {}'.format((nota1 + nota2)/2))