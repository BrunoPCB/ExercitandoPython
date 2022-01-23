"""
17 - Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
"""

n = input("Informe um número inteiro, e mostraremos seu fatorial: ")
total = 1

try:
    n = int(n)

    for i in range(n, 0, -1):
        total *= i

    print(total)
except:
    print("Erro, tipo de dado informado inválido.")
