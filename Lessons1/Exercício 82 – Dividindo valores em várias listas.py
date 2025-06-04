lista = []
pares = []
impares = []
for i in range(10):
    valor = int(input('Digite um numero: '))
    lista.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
print(lista)
print(pares)
print(impares)


