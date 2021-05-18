"""
5  - Faça um programa para a leitura de duas notas parciais de um aluno.
     O programa deve calcular a média alcançada por aluno e apresentar:
        A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
        A mensagem "Reprovado", se a média for menor do que sete;
        A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

notas = []

notas.append(input("Informe a primeira nota: "))
notas.append(input("Informe a segunda nota: "))

media = (float(notas[0]) + float(notas[1])) / len(notas)

if media >= 7:
    print("APROVADO")
elif media < 7:
    print("REPROVADO")
elif media == 10:
    print("APROVADO COM DISTINÇÃO")

