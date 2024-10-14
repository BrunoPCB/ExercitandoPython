"""
32 - Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
    Fatorial de: 5
    5! =  5 . 4 . 3 . 2 . 1 = 120
"""

numero_fatorial = int(input('Informe o valor que deseja calcular o fatorial: '))
resultado_fatorial = f'{numero_fatorial}! = '
fatorial = 1
numero_final = 1

for numero in range(numero_fatorial, numero_final, -1):
    resultado_fatorial = resultado_fatorial + f'{numero}'

    fatorial = fatorial * numero

    if numero != numero_final:
        resultado_fatorial = resultado_fatorial + ' . '

resultado_fatorial = resultado_fatorial + f' = {fatorial}'

print(resultado_fatorial)