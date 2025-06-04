palavras_aleatorias = ('maçã', 'carro', 'livro', 'céu', 'gato', 'futebol', 'árvore', 'caneta', 'computador', 'jardim')
vogais = 'aeiou'

# Percorre cada palavra na tupla
for palavra in palavras_aleatorias:
    # Para cada palavra, conta quantas vezes cada vogal aparece
    for vogal in vogais:
        if vogal in palavra:
            print(f"A vogal '{vogal}' aparece {palavra.count(vogal)} vez(es) na palavra '{palavra}'.")
