# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
ano = int(input('Digite um ano, Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano %4 == 0 and ano %100 !=0 or ano % 400 == 0:
    print(f'O ano de {ano} é BISSEXTO')
else:
    print(f'O ano de {ano} NAO é BISSEXTO')
