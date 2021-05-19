"""
6  - Faça um Programa que leia três números e mostre o maior deles.
"""

numeros = []

numeros.append(float(input("Informe o 1º número: ")))
numeros.append(float(input("Informe o 2º número: ")))
numeros.append(float(input("Informe o 3º número: ")))

if numeros[0] > numeros[1] and numeros[0] > numeros[2]:
    print(f"{numeros[0]} é o maior")

elif numeros[0] < numeros[2] and numeros[1] < numeros[2]:
    print(f"{numeros[2]} é o maior")

elif numeros[1] > numeros[0] and numeros[1] > numeros[2]:
        print(f"{numeros[1]} é o maior")

else:
    print("Todos os valores são iguais")
