"""
8 - Faça um programa que leia 5 números e informe a soma e a média dos números.
"""

numeros = []
total = 0

for i in range(5):
    numeros.append(input("Informe um número: "))
    try:
        numeros[i] = int(numeros[i])
    except:
        print("Erro")

for value in numeros:
    print(f"{total} + {value}")
    total += value
    

print(f"Soma total: {total}")