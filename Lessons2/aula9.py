#Faça um Programa que leia um vetor de 5 números inteiros
# e mostre-os.criar lista vetor vazia
vetor = []
for i in range(5):
    while True:
        try:
            num = int(input(str(i + 1) + ") Digite um número:"))
            break
        except:
            print('Digite simente números inteiros')
    vetor.append(num)
print(vetor)