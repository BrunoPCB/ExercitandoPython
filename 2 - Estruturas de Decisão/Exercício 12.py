"""
12 - Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
"""

dias_da_semana = {1: 'Domingo', 2: 'Segunda', 3: 'Terça', 4: 'Quarta', 5: 'Quinta', 6: 'Sexta', 7: 'Sábado'}

numero = int(input("Digite um número referente a um dia da semana: "))

if numero < 0 or numero > 7:
    print("Número inválido")
else:
    print(f"O dia da semana referente ao número {numero} é {dias_da_semana[numero]}")
