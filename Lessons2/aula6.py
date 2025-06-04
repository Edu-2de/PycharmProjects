#Ler 10 números, mas encerra quando receber um número negativo
for i in range(10):
    n = int(input(str(i) + 'Digite um número: '))
    if n<0:
        break
        menor=n
    print(f'Encerrou com i={i} e n={n}')
