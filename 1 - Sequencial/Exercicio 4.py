"""
4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""

# Pedir 4 notas ao usuário
num_1 = int(input("Primeira nota: "))
num_2 = int(input("Segunda nota: "))
num_3 = int(input("Terceira nota: "))
num_4 = int(input("Quarta nota: "))

# Realizando o cálculo de média.
# O cálculo de média é (soma todas notas) / quantidade de notas.
media = (num_1 + num_2 + num_3 + num_4) / 4

# informando as notas e a média.
print(f"A média das seguintes notas : {num_1}, {num_2}, {num_3}, {num_4}é {media:.2f}")
