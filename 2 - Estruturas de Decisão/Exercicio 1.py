"""
1  - Faça um Programa que peça dois números e imprima o maior deles.
"""
numero_1 = input("Informe um número: ")
numero_2 = input("Informe outro número: ")

numero_1 = float(numero_1)
numero_2 = float(numero_2)

if numero_1 > numero_2:
    print(f"{numero_1} é maior que {numero_2}")
else:
    print(f"{numero_2} é maior que {numero_1}")
