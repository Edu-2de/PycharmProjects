num = int(input('Digite um número: '))
while num >0:
    for i in range(10):
        print(f'{num} * {i+1} = {num*(i+1)}')
    num = int(input('Digite um número: '))
else:
    print('FIM')