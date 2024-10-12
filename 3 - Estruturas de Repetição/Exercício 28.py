"""
28 - Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto
     em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
"""
quantidade_cds = int(input('Quantos CDs tem na coleção: '))
precos_cds = {}
valor_total_cds = 0

for cd in range(quantidade_cds):
    valor_cd = float(input(f'Quanto custa o CD {cd+1}: '))
    precos_cds[cd] = valor_cd
    valor_total_cds = valor_total_cds + valor_cd

valor_medio_cds = valor_total_cds / quantidade_cds

print(f'Valor total dos CDs é de R${valor_total_cds:.2f}\n'
      f'Valor médio de todos CDs é de R${valor_medio_cds:.2f}')


