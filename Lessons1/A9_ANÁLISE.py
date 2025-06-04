print('###########################')


frase = "Curso em video Python"

# Esse comando serve para: ver quantos carácteres tem uma frase.
print(len(frase))


print('###########################')


# Esse comando serve para: contar quantas vezes aparecem determinados carácteres.
print(frase.count('o'))


print('###########################')


# E além de somente contar, o (conut) também pode contar quantas vezes aparecem determinados carácteres, em um fatiamento específico.(ou seja ele vai contar quantas vezes aprece 'o', do carácter 0 até o 12.
print(frase.count('o',0,13))


print('###########################')


# Esse comando serve para: encontrar a quantidade de vezes que uma palavra apareceu, e ele mostra na tela em qual posicao que tal palavra ou carácter apareceu, nesse caso o 'deo' comecou a aparecer na posicao 11
print(frase.find('deo'))


print('###########################')


# Existe também o caso de pedir ao find para encontrar uma palavra ou carácter que nao esteja dentro da nossa frase, nesse caso ele retornará como -1, pois ele nao existe, logo também a posicao -1 nao existe já que comecam a contar na posicao 0
print(frase.find('Android'))


print('###########################')


# Esse comando serve para: saber se dentro da nossa frase existe uma palavra ou carácter específicos, sempre retornando como true ou false
print('Curso' in frase)