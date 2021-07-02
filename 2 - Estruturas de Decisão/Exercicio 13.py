"""
13 - Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
      Média de Aproveitamento  Conceito
      Entre 9.0 e 10.0        A
      Entre 7.5 e 9.0         B
      Entre 6.0 e 7.5         C
      Entre 4.0 e 6.0         D
      Entre 4.0 e zero        E
    O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se
    o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

"""
notas = []
aproveitamento = ''
aluno = {"nota": [], "aproveitamento": '', "media": 0, "Conceito": ''}

notas.append(int(input("Informe a primeira nota: ")))
notas.append(int(input("Informe a segunda nota: ")))

aluno["notas"] = notas

media = sum(notas) / len(notas)

aluno["media"] = media

if (media > 9) and (media <= 10):
    aproveitamento = 'A'
    conceito = 'APROVADO'
elif (media > 7.5) and (media <= 9):
    aproveitamento = 'B'
    conceito = 'APROVADO'
elif (media > 6) and (media <= 7.5):
    aproveitamento = 'C'
    conceito = 'APROVADO'
elif (media > 4) and (media <= 6):
    aproveitamento = 'D'
    conceito = 'REPROVADO'
else:
    aproveitamento = 'E'
    conceito = 'REPROVADO'

aluno["aproveitamento"] = aproveitamento
aluno["conceito"] = conceito

print("------------------------------------------")
for enum, nota in enumerate(aluno['notas'], 1):
    print(f"{enum}ª Nota: {nota}")

print(f"Media: {aluno['media']}")
print(f"Aproveitamento: {aluno['aproveitamento']}")
print(f"Conceito: {aluno['conceito']}")
print("------------------------------------------")