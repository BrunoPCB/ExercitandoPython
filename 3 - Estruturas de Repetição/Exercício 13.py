"""
13 - Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro 
    número elevado ao segundo número. Não utilize a função de potência da linguagem.
"""

b = input("Informe um valor base: ")
e = input("Informe um valor expoente: ")

try:
    b = int(b)
    e = int(e)
    print(f"{b} elevado a {e} é igual a {b**e}")
except:
    print("Erro")

