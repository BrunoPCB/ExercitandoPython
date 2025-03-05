"""
38 - Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
    a. Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
    b. Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
    c. A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
    Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo
    que o usuário digite o salário inicial do funcionário.
"""

from datetime import date

ano_incio_contrato = int(input('Informe o ano que iniciou a trabalhar na empresa: '))
salario_inicial = float(input('Informe o salário inicial: '))
aumento_inicial = float(input('Informe o aumento inicial: '))

ano_atual = date.today().year
tempo_trabalho = ano_atual - (ano_incio_contrato + 1)
aumento = aumento_inicial

for num in range(1, tempo_trabalho+1):
    aumento *= 2

aumento /= 100

salario_atual = aumento + salario_inicial

print(f'Seu salário atual é de {salario_atual:.2f}.')