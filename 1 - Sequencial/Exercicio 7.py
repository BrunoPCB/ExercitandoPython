"""
7 - Faça um Programa que calcule a área de um quadrado,
em seguida mostre o dobro desta área para o usuário.
"""
# Recebe o lado do quadrado.
from abc import abstractclassmethod

lado = int(input("Qual o lado do quadrado? "))

# Clacular a área do quadrado
area = pow(lado, 2)  # area = lado ao quadrado

# Imprimir resultado
print(f"A área do quadrado com lado {lado} é igual a {area}")