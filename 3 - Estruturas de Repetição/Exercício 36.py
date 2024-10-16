"""
36 - Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada
     não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário,
     conforme exemplo abaixo:

    Montar a tabuada de: 5
    Começar por: 4
    Terminar em: 7

    Vou montar a tabuada de 5 começando em 4 e terminando em 7:
    5 X 4 = 20
    5 X 5 = 25
    5 X 6 = 30
    5 X 7 = 35
    Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.

"""

numero_tabuada = int(input('Montar a tabuada de: '))
numero_comecar = int(input('Começar em: '))
numero_terminar = int(input('Terminar em: '))

if numero_comecar > numero_terminar:
    numero_final_valido = False

    while not numero_final_valido:
        print('Número final deve ser maior que o inicial.')
        numero_terminar = int(input('Terminar em: '))

        if numero_comecar < numero_terminar:
            numero_final_valido = True



print('---' * 5)
print(f'TABUADA DE {numero_tabuada}')
print('---' * 5)

for numero in range(numero_comecar, numero_terminar+1):
    print(f'{numero} X {numero_tabuada} = {numero * numero_tabuada}')

print('---' * 5)