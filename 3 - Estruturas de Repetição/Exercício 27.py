"""
27 - Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a
     quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
"""

quantidade_turmas = 5
media_alunos = 0

for turma in range(quantidade_turmas):
    quantidade_alunos_permitida = False

    while not quantidade_alunos_permitida:
        quantidade_alunos = int(input(f'Quantos alunos tem na turma {turma+1}: '))

        if quantidade_alunos <= 40:
           quantidade_alunos_permitida = True
           media_alunos = media_alunos + quantidade_alunos
        else:
            quantidade_alunos_permitida = False
            print('Turma precisa ter no máximo 40 alunos')

media_alunos = media_alunos / quantidade_turmas

print(f'A média de alunos das {quantidade_turmas} turmas é {media_alunos}.')