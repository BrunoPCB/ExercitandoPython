"""
26 - Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor
     votar e ao final mostrar o número de votos de cada candidato.
"""
quantidade_eleitores = 15
candidatos = [13, 22, 17]
votos = {13: 0,
         22: 0,
         17: 0}

for eleitor in range(quantidade_eleitores):
    votou = False
    while not votou:
        print('Vote em um dos candidatos abaixo\n'
              '[13] - Juscélio\n'
              '[22] - Terezinha\n'
              '[17] - Josefino')
        voto = int(input('Vote aqui: '))

        if voto in candidatos:
            votou = True
        else:
            print('Vote novamente')

    votos[voto] = votos[voto] + 1

print('Quantidade de votos de cada candidato apurado\n'
      f'[13] - {votos[13]}\n'
      f'[22] - {votos[22]}\n'
      f'[17] - {votos[17]}\n')