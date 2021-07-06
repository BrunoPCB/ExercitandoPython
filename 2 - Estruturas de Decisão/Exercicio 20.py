"""
20 - Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque
     e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de
     1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve
     se preocupar com a quantidade de notas existentes na máquina.
        Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50,
        uma nota de 5 e uma nota de 1;
        Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50,
        quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""


def separa_algarismos(num):
    unidade = num // 1 % 10
    dezena = num // 10 % 10 * 10
    centena = num // 100 % 10 * 100

    return unidade, dezena, centena


notas_disponiveis = [1, 5, 10, 50, 100]

valor = int(input("Mínimo: R$ 10,00 | Máximo: R$ 600,00\n"
                  "Informe um valor para saque: "))

if valor < 10 or valor > 600:
    print("O valor de saque informado deve estar entre 10 e 600")
else:
    valor_sep = {"unidade": 0, "dezena": 0, "centena": 0}
    resultado = ''
    passou = False
    # Separar valores total
    valor_sep["unidade"], valor_sep["dezena"], valor_sep["centena"] = separa_algarismos(valor)

    if 10 > valor_sep["unidade"] > 0:
        notas_5 = valor_sep['unidade'] // 5
        if valor_sep["unidade"] == 5:
            resultado = f"{notas_5} notas de 5"
        elif 5 > valor_sep["unidade"] > 0:
            resultado = f"{valor_sep['unidade']} notas de 1"
        else:
            resultado = f"{notas_5} notas de 5 e {valor_sep['unidade'] - (notas_5 * 5)} notas de 1"
        passou = True

    if valor_sep["dezena"] < 100 and valor_sep["dezena"] >= 10:
        # Se passou na verificação anterior adiciona uma linha
        if passou: resultado += "\n"

        notas_50 = valor_sep['dezena'] // 50
        if valor_sep['dezena'] == 50:
            resultado += f"{notas_50} notas de 50"
        elif 50 > valor_sep["dezena"] >= 10:
            resultado += f"{valor_sep['dezena'] // 10} notas de 10"
        else:
            resultado += f"{notas_50} notas de 50 e {(valor_sep['dezena'] - (notas_50 * 50)) // 10} notas de 10"
        passou = True

    if valor_sep["centena"] >= 100:
        notas_100 = valor_sep["centena"] // 100
        if passou: resultado += "\n"
        resultado += f"{notas_100} notas de 100"

    print(resultado)
