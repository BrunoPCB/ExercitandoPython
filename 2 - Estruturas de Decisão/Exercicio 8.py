"""
8  - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""


numeros = []

print("Informe o preço de três produtos")
numeros.append(float(input("Informe o preço do 1º produto: ")))
numeros.append(float(input("Informe o preço do 2º produto: ")))
numeros.append(float(input("Informe o preço do 3º produto: ")))

if numeros[0] > numeros[1] > numeros[2]:
    print(f"O produto com preço R${numeros[2]:.2f} é mais barato")

elif numeros[0] < numeros[1] < numeros[2]:
    print(f"O produto com preço R${numeros[0]:.2f} é mais barato")

elif (numeros[1] < numeros[0] < numeros[2]) or (numeros[1] < numeros[2] < numeros[0]):
    print(f"O produto com preço R${numeros[1]:.2f} é mais barato")

else:
    print("2 ou mais produtos tem preços iguais")

