"""
24 - Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

        "Telefonou para a vítima?"
        "Esteve no local do crime?"
        "Mora perto da vítima?"
        "Devia para a vítima?"
        "Já trabalhou com a vítima?"

        O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
        Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
        entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
        Caso contrário, ele será classificado como "Inocente".
"""

questionario = {"Telefonou para a vítima?": False,
                "Esteve no local do crime?": False,
                "Mora perto da vítima?": False,
                "Devia para a vítima?": False,
                "Já trabalhou com a vítima?": False}

contar = 0

for key, value in questionario.items():
    print(key)
    print("(1) Sim\n"
          "(2) Não")
    questionario[key] = True if input("Sua escolha: ") == '1' else False

for valor in questionario.values():
    if valor:
        contar += 1


if contar == 2:
    print("Você é um Suspeito.")
elif 4 > contar >= 3:
    print("Você é um Cúmplice.")
elif contar == 5:
    print("Você é o Assassino.")
else:
    print("Você é Inocente.")

