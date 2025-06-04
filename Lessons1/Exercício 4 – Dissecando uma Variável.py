# Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informacoes possíveis sobre ele.

algo = input('Digite algo: ')

# Diz se é uma letra ou um número.
print("{} é alfa-numérico? {}".format(algo, algo.isalnum()))

# Diz se tem apenas letras do alfabéto
print("{} é alfabético? {}".format(algo, algo.isalpha()))

# Diz se é um ASCII, (A tabela ASCII)
print("{} é ASCII? {}".format(algo, algo.isascii()))

# Diz se todos os caracteres sao dígitos.
print("{} é um dígito? {}".format(algo, algo.isdigit()))

# Diz se os carácteres sao imprimíveis.
print("{} é imprimível? {}".format(algo, algo.isprintable()))

# Diz se todos os caracteres forem espacos em branco.
print("{} é um espaco? {}".format(algo, algo.isspace()))

# Diz se todos os caracteres são válidos para escrever um identificador no código, conforme a lista.
print("{} é um identificador? {}".format(algo, algo.isidentifier()))

# Diz se todos os caracteres estao em minúsculo.
print("{} é minúsculo? {}".format(algo, algo.islower()))

# Diz se todos os caracteres estao em maiúsculo
print("{} é  maiúsculo? {}".format(algo, algo.isupper()))




