"""
7 - Faça um programa que leia 5 números e informe o maior número.
"""

numeros = []
maior = 0

for i in range(5):
    numeros.append(input("Informe um número: "))
    try:
        numeros[i] = int(numeros[i])
    except:
        print("Erro")


numeros.sort(reverse=True)

maior = numeros[0]

print(f"O maior número é {maior}.")