"""
11 - Altere o programa anterior para mostrar no final a soma dos números.
"""

a = input("Informe o primeiro valor: ")
b = input("Informe o segundo valor: ")
soma = 0

try:
    a = int(a)
    b = int(b)
except:
    print("Erro")

if a > b:
    print("O valor inicial informado é maior que o valor final.")

for valor in range(a+1, b):
    print(valor)
    soma += valor

print(f"A soma dos valores é igual a {soma}")