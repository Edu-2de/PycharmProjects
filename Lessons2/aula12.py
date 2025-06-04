#DEFinição de função sem parâmetros
def listaTurma():
    print(f"{'Nome':^18} | {'Nota':^6} | ")
    print(f"{'-' * 18} | {'-' * 6} |")
    for i in range(len(alunos)):
        print(f"{alunos[i]:^18} | {notas[i]:^6} |")

alunos=['Talita', 'Eduardo','Pedro H','Gabriel']
notas=[8, 5,7.5,10]
while True:
    while True:
        try:
            print('\nMENU de escolha\n')
            print('   (1) cadastra alunos e medias')
            print('   (2) lista todos alunos e medias')
            print('   (3) busca um aluno e sua nota')
            print('   (4) calcula média da turma')
            print('   (5) fim')
            opcao=int(input('Opção:'))
            break
        except:
            print('Digite somente valores de números 1 até 5')
    if opcao==5:
        break
    elif opcao==1: # cadastro alunos e notas  nas listas
        nome = input('\nDigite nome do aluno(a) [ENTER] Encerra:')
        while nome:
            try:
                nota=float(input('Digite nota de '+nome+':'))
                alunos.append(nome)
                notas.append(nota)
                nome = input('\nDigite nome do aluno(a) [ENTER] Encerra:')
            except:
                print('Digite notas em núm,eros REAIS (FLOAT)')
    elif opcao==2:  # lista alunos e notas
        listaTurma()
        input('[ENTER] Continua')
    elif opcao==3:
        listaTurma()
        nome=input('Digite Nome Aluno Ver a nota:')
        i=alunos.index(nome)
        print(f"{alunos[i]:^18} | {notas[i]:^6} |")
        input('[ENTER] Continua')

    elif opcao==4:
        listaTurma()
        media=sum(notas)/len(notas)
        print('{0:45}{1:10}'.format('Média de Turma:',media))
        input('[ENTER] Continua')
print('Fim Programa')