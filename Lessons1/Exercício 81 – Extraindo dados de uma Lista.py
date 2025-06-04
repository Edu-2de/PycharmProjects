lsita = []
for palavra in range(5):
    palavra = int(input('Digite um numero: '))
    lsita.append(palavra)
print(lsita)
print(len(lsita))
if 5 in lsita:
    print('5 esta na lista')
else:
    print('5 nao esta na lista')