"""
34 - Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é
     aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se
     ele é ou não um número primo.
"""
numero = int(input('Informe um número: '))
eh_primo = True

for num in range(numero, 1, -1):
    if not num in [1, numero]:
        eh_primo = (numero % num != 0)

print(f'O número {numero}{' NÃO' if not eh_primo else ''} é primo')