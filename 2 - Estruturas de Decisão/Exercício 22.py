"""
22 - Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
"""
numero = float(input("Informe um número: ").replace(',', '.'))

if numero // 1 == numero:
    print("Número inteiro.")
else:
    print("Número decimal.")
