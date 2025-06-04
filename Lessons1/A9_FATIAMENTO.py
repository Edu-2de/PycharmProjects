# Fatiamento de string: aqui vamos fatiar uma string, para tal acao é necessário saber que a frase abaixo tem um total de 20 caracteres contando com os epacos sempre.

frase = "Curso em video Python"

# logo o print abaixo irá somente mostrar a palavra: vide, pois colocamos que ele deve mostrar do carácter 9 até o carácter 13, ele nao mostra o 'o' pois sempre acaba um carácter antes
print(frase[9:13])


print('###########################')


# Mesmo sabendo que sao 20 caracteres essa frase, colocando para acabar no 21 irá dar o resultado esperado, que é até o final, ou seja irá mostrar do carácter 9 até o 20
print(frase[9:21])


print('###########################')


# Aqui ele irá mostrar praticamente o mesmo resultado do exemplo acima, mas dessa vez pulando de 2 em 2 os carácteres.
print(frase[9:21:2])


print('###########################')


# Mesmo sem especificar de onde o fatiamento vai comecar, o comando funciona do mesmo jeito, ou seja, sem especificar de onde quer que o fatiamento comece, o programa irá comecar automaticamente do carácter 0
print(frase[:5])


print('###########################')


# Da mesma forma funciona para o final do fatiamento, quando nao queremos especificar-lo, o programa entenderá que é necessário fatiar até o final.
print(frase[15:])


print('###########################')