"""
19 - Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
"""

from typing import Type


n = input("informe a quantidade de números da coleção: ")

try:
    n = int(n)

    numeros = []

    while(len(numeros) < n):
        num = input("informe um número: ")
        try:
            num = int(num)
            if 0 < num < 1000:
                numeros.append(num)
        except TypeError as te:
            print("Type: ", te)
        except ValueError as ve:
            print("Value: ", ve)
        except Exception as e:
            print("Erro: ", e)

    if len(numeros) > 0:
        numeros.sort()


        print("O menor valor: ", numeros[0])
        print("O maior valor: ", numeros[len(numeros)-1])


except ValueError as e:
    print("Erro no tipo de  dados. Erro: ", e)
