# Usando listas 
# Faça um algoritmo que leia o nome e a idade de um conjunto
# de nadadores e, a partir da idade classifique-os em uma das
# seguintes categorias:
# infantil A = 5 - 7 anos
# infantil B = 8-10 anos
# juvenil A = 11-13 anos
# juvenil B = 14-17 anos
# adulto = maiores de 18 anos
# O programa deve terminar quando o nome for = “FIM”
nome = []
idade = []
categoria = []
n = input("Digite nome do NADADOR")
while n.lower() != 'fim':
    i = int(input("Digite a idade do(a) " + n))
    if i >= 5 and i <= 7:
        c = 'Infantil A'
    elif i >= 8 and i <= 10:
        c = 'Infantil B'
    elif i >= 11 and i <= 13:
        c = 'Juvenil A'
    elif i >= 14 and i <= 17:
        c = 'Juvenil B'
    elif i >= 18:
        c = 'Adulto'
    nome.append(n)
    idade.append(i)
    categoria.append(c)
    n = input("Digite nome do NADADOR")
for i in range(len(nome)):
    print(i, 'Nome: ', nome[i], idade[i], categoria[i])
print("Adulto: ", categoria.count("Adulto"))
print("Juvenil B ", categoria.count("Juvenil B"))
print("Juvenil A ", categoria.count("Juvenil A"))
print("Infantil A ", categoria.count("Infantil A"))
print("Infantil B ", categoria.count("Infantil B"))
print("@@@@@@@@@@ Adulto @@@@@@@@@")
somaIdade = 0
cont = 0
for i in range(len(categoria)):
    if categoria[i] == "Adulto":
        print(nome[i], " idade ", idade[i])
        somaIdade = somaIdade + idade[i]
        cont += 1
print("Media idade Adultos = ", somaIdade / cont)

print("@@@@@@@@@@ Juvenil B @@@@@@@@@")
for i in range(len(categoria)):
    if categoria[i] == "Juvenil B":
        print(nome[i], " idade ", idade[i])
#### continue a partir daqui 