"""
21 - Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
     Um número primo é aquele que é divisível somente por ele mesmo e por 1.
"""

numero = input("Informe um número: ")
primo = False

try:
    numero = int(numero)

    cont = 0
    for j in range(1, numero+1):
        if numero % j == 0:
            cont += 1
    
    if cont <= 2:
        primo = True

except Exception as e:
    print("Error: ", e)

if primo:
    print(f"O número {numero} é um número PRIMO.")
else:
    print(f"O número {numero} é um número NÃO é primo.")