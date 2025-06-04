# Faca um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor.

numero = int(input('Digite um número: '))


# Aqui usamos a soma e subtracao, dentro do (print()) no (.format())

print('O número {} tem com sucessor: {} e como antecessor: {}'.format(numero, numero+1, numero-1))
