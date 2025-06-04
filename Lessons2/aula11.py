#Faça um Programa que leia um vetor de 10 números reais
# e mostre-os na ordem inversa.
# versao 1
vetor=[]
for i in range(1,11):
    while True:
        try:
            num=float(input( str(i) + ") Digite um número:"))
            break
        except:
            print('Digite somente números reais (FLOAT)')
    vetor.append(num)
print('Vetor na ordem de entrada')
print(vetor)
print()
print('Vetor na ordem invertida')
for i in range (-1,-11,-1):
    print(f' {i} <=>{len(vetor) - (i * -1) + 1} <=>{len(vetor) - (i * -1) }==> {vetor[i]}   índice verdadeiro=> {i}  ')
