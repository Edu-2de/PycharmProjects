# faça um progrma que liste os numeros de 0 a 100

for i in range(101):
    print(i)
print('FIM')


# Esse vai rodar até o número 19, porque ele sempre tira um, para rodar até 20, teria que ser 21

for i in range(5,20):
    print(i)
print('FIM')


# Esse 2 que colocamos do lado do 21, serve para exibir os numeros em pares de 2

for i in range(0,21,2):
    print(i)
print('FIM')


#numeros impares de 0 a 15

print('impares')
for i in range (0,16,1):
    if i % 2 == 1:
        print(i)
