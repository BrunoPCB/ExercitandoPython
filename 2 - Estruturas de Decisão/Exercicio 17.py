"""
17 - Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
"""

meses = {1: {"janeiro": 31},
         2: {"fevereiro": 28},
         3: {"março": 31},
         4: {"abril": 30},
         5: {"maio": 31},
         6: {"junho": 30},
         7: {"julho": 31},
         8: {"agosto": 31},
         9: {"setembro": 30},
         10: {"outubro": 31},
         11: {"novembro": 30},
         12: {"dezembro": 31}}

dia = int(input("Informe um dia: "))
mes = int(input("Informe um mes: "))
ano = int(input("Informe um ano: "))

contador = [x for x in range(1, len(meses))]

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    meses[2]["fevereiro"] = 29


for cont, items in meses.items():
    if mes == cont:
        for key, value in items.items():
            if (dia > 0) and (dia <= value):
                data = str(dia) + "/" + str(mes) + "/" + str(ano)
                print(data)
            else:
                print(f"Este dia não está dentro do mês de {key}")

