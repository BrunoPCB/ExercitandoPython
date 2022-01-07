"""
6 - Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
    Depois modifique o programa para que ele mostre os números um ao lado do outro.
"""

print("Coluna\n")

for i in range(20):
    print(i+1)

print("\nLinha\n")

for i in range(20):
    print(i+1, end=" ")

print()