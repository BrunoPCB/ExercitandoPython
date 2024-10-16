"""
35 - Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.
"""

quantidade_numeros_primos_procurar = int(input('Informe a quantidade de números primos procurar: '))
numeros_primos = []
eh_primo = False
quantidade_numeros_divisiveis = 0

for numero in range(1, quantidade_numeros_primos_procurar+1):
    quantidade_numeros_divisiveis = 0

    for num in range(numero, 0, -1):
        if numero % num == 0:
           quantidade_numeros_divisiveis += 1

        eh_primo = (quantidade_numeros_divisiveis == 2)

    if eh_primo:
        numeros_primos.append(numero)


print(f'Números primos de 1 até {quantidade_numeros_primos_procurar}:'
      f'{numeros_primos}')