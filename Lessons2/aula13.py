def listanadadores():
    print(f"{'Nome':^18} | {'Idade':^6} | ")
    print(f"{'-' * 18} | {'-' * 6} |")
    for i in range(len(nomes)):
        print(f"{nomes[i]:^18} | {idades[i]:^6} |")

nomes = []
idades = []
infantil_a = []
infantil_b = []
juvenil_a = []
juvenil_b = []
adulto = []


while True:
    while True:
        try:
            print('\nMENU de escolha\n')
            print('   (1) cadastrar nomes e idades')
            print('   (2) listar numero de participantes')
            print('   (3) listar o nome de todos de participantes por categoria e a idade de cada participante.')
            print('   (4) média de idades de cada categoria.')
            print('   (5)  FIM.')
            opcao = int(input('Opção:'))
            break
        except:
            print('Digite somente valores de números 1 até 6')
    if opcao == 5:
        break
    elif opcao == 1:
        nome = input('\nDigite nome do nadador [ENTER] Encerra:')
        while nome:
            try:
                idade = int(input('Digite idade de '+nome+':'))
                if idade == 5 or idade == 6 or idade == 7:
                    infantil_a.append(idade)
                    idades.append(idade)
                    nomes.append(nome)
                elif idade == 8 or idade == 9 or idade == 10:
                    infantil_b.append(idade)
                    idades.append(idade)
                    nomes.append(nome)
                elif idade == 11 or idade == 12 or idade == 13:
                    juvenil_a.append(idade)
                    idades.append(idade)
                    nomes.append(nome)
                elif idade == 14 or idade == 15 or idade == 16 or idade == 17:
                    juvenil_b.append(idade)
                    idades.append(idade)
                elif idade > 18:
                    adulto.append(idade)
                    idades.append(idade)
                    nomes.append(nome)
                elif idade < 5:
                    print('DIGITE SOMENTE IDADES MAIORES QUE 5')
                    break
                nome = input('\nDigite nome do nadador [ENTER] Encerra:')
            except:
                print('DIGIE SOMENTE NOMES!!')
    elif opcao == 2:
        print(f' infantil A = 5 - 7 anos, tem:{len(infantil_a)} nadadores')
        print(f'  infantil B = 8 - 10 anos, tem:{len(infantil_b)} nadadores')
        print(f'  juvenil A = 11 - 13 anos, tem:{len(juvenil_a)} nadadores')
        print(f'  juvenil B = 14 - 17 anos, tem:{len(juvenil_b)} nadadores')
        print(f'  adulto = maiores de 18 anos, tem:{len(adulto)} nadadores')
        input('[ENTER] Continua')
    elif opcao == 3:
        listanadadores()
        input('[ENTER] Continua')
    elif opcao == 4:
        listanadadores()
        media = sum(idades)/len(idades)
        print('{0:45}{1:10}'.format('Média de nadadores:',media))
        input('[ENTER] Continua')
print('Fim Programa')


