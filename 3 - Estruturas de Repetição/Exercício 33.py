"""
33 - O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado
     de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
"""

quantidade_temperaturas = int(input('Informe a quantidade de temperaturas: '))
media_temperaturas = 0
temperaturas = []

for temperatura in range(quantidade_temperaturas):
    temperaturas.append(float(input(f'Informe a {temperatura+1}ª temperatura: ')))
    media_temperaturas = media_temperaturas + temperaturas[temperatura]

media_temperaturas = media_temperaturas / quantidade_temperaturas

temperaturas.sort()

print(f'Maior temperatura: {temperaturas[-1]}\n'
      f'Menor temperatura: {temperaturas[ 0]}\n'
      f'Média temperaturas: {media_temperaturas}')
