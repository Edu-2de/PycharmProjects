#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

idade = int(input('QUAL ANO VOCE NASCEU? '))
calc = 2024 - idade

if calc == 18:
    print('VOCE DEVE SE ALISTAR AGORA')
elif calc > 18:
    saldo = calc - 18
    print(f'VOCE PERDEU O TEMPO DO SEU ALISTAMENTO, DEVERIA TER SIDO FEITO EM {saldo} anos')
elif calc < 18:
    saldo = 18 - calc
    print(f'VOCE AINDA NAO DEVE SE ALISTAR,FLATAM {saldo} anos')
