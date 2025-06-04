#teste = []
#teste.append('Gustavo')
#teste.append('40')
#galera = []
#galera.append(teste[:])
#teste[0] = 'maria'
#teste[1] = 22
#galera.append(teste[:])
#print(galera[0])


#galera = [['Joao', 19], ['Ana', 33], ['Joaquim', 45], ['Maria', 45]]
#for p in galera:
#    print(p[0])

galera = []
dado = []
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)