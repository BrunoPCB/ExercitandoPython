"""
10 - Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo 
     compreendido por eles.
"""


a = input("Informe o primeiro valor: ")
b = input("Informe o segundo valor: ")

try:
    a = int(a)
    b = int(b)
except:
    print("Erro")

if a > b:
    print("O valor inicial informado é maior que o valor final.")

for valor in range(a+1, b):
    print(valor)

