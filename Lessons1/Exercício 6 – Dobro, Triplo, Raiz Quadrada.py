# Crie um algorítimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero = int(input('Digite um número: '))

# Aqui usamos a multiplicacao que é definida por: (*) e a potenciacao que é definida por: (**), usamos a potencia nesse caso para definir a raiz quadrada, ja que se elevarmos a meio, sonseguimos a mesma
print('O número: {} tem como dobro: {}, triplo: {} e raiz quadrada: {}'.format(numero, numero * 2, numero * 3,
                                                                               numero ** 1 / 2))
