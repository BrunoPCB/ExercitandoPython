"""
34 - Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é
     aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se
     ele é ou não um número primo.
"""
numero = int(input('Informe um número: '))
eh_primo = False
quantidade_numeros_divisiveis = 0

for num in range(numero, 0, -1):
    if numero % num == 0:
        quantidade_numeros_divisiveis += 1

eh_primo = (quantidade_numeros_divisiveis == 2)

print(f'O número {numero}{" NÃO" if not eh_primo else ""} é primo')