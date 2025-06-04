#Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

#a) Os 5 primeiros times.

#b) Os últimos 4 colocados.

#c) Times em ordem alfabética.

#d) Em que posição está o time da Chapecoense.


times_brasileirao = (
    "Botafogo", "Palmeiras", "Fortaleza", "Flamengo", "São Paulo",
    "Internacional", "Bahia", "Cruzeiro", "Atlético Mineiro", "Vasco",
    "Grêmio", "Criciúma", "Red Bull Bragantino", "Juventude",
    "Athletico Paranaense", "Fluminense", "Vitória", "Corinthians",
    "Cuiabá", "Atlético Goianiense"
)
times_enumerados = list(enumerate(times_brasileirao, start=1))

print(f'Os primeiros 5 colocados sao: {times_brasileirao[0:5]}')
print(f'Os ultimos 4 colocados sao: {times_brasileirao[16:20]}')
print(f'Os times em ordem alfabetica sao: {sorted(times_brasileirao)}')

time = str(input("Qual time voce deseja saber a posicao? "))
if time in times_brasileirao:
    for posicao, nome_time in times_enumerados:
        if nome_time == time:
            print(f'O seu time está na {posicao}ª posição.')
else:
    print('Seu time não está classificado entre os 20 principais.')


