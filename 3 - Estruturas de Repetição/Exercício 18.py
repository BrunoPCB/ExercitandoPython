"""
18 - Faça um programa que, 
     dado um conjunto de N números,
     determine o menor valor, 
     o maior valor e a soma dos valores.
"""

n = input("informe a quantidade de números da coleção: ")

try:
    n = int(n)

    numeros = []

    for i in range(n):
        numeros.append(input("informe um número: "))
    

    if len(numeros) > 0:
        numeros.sort()


        print("O menor valor: ", numeros[0])
        print("O maior valor: ", numeros[len(numeros)-1])


except ValueError as e:
    print("Erro no tipo de  dados. Erro: ", e)
