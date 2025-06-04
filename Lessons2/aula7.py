contador = 1
senha = input('DIgite a senha: ')

while senha !='senac0202020202020202':
    print(f'Senha errada {contador}/3')
    if contador >= 3:
        print('Excesso')
        break
    senha=input('Digite a senha: ')
    contador+=1


else:
    print("Senha certa")
