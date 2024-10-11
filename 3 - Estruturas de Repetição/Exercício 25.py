"""
    25 - Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60
         e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
"""
quantidade_pessoas = 5
pessoas_idades = {}
turma = ''
media_idades = 0

for indice in range(5):
    pessoa = input('Qual seu nome: ')
    idade = int(input('Qual sua idade: '))

    media_idades = media_idades + idade

    pessoas_idades[pessoa] = idade

media_idades = media_idades / quantidade_pessoas

if 0 < media_idades < 25:
    turma = 'Jovem'
elif 26 < media_idades < 60:
    turma = 'adulta'
else:
    turma = 'idosa'

print('A turma é ' + turma)
