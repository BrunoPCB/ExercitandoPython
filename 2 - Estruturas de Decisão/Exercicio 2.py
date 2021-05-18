"""
2  - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""
numero = input("Informe um número: ")

if numero == '0' or numero == '-0':
    numero = '0'

numero = float(numero)

if numero >= 0:
    print(f"{numero} é POSITIVO")
else:
    print(f"{numero} é NEGATIVO")
